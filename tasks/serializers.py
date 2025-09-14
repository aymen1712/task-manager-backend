from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from accounts.models import User
from projects.models import Project
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, allow_null=True)
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status', 'priority', 'due_date', 'created_by', 'assigned_to',
                  'project')
        read_only_fields = ('id', 'created_at')

    def validate(self, data):
        assigned_to = data.get('assigned_to', None)
        project = data.get('project')
        request_user = self.context['request'].user

        if not project:
            raise ValidationError("A project is required.")

        if assigned_to:
            if request_user != project.created_by or request_user.role != 'admin':
                if assigned_to not in project.members.all():
                    raise ValidationError("You are not authorized to perform this action.")
        return data

    def create(self, validated_data):
        assigned_to = validated_data.get('assigned_to', None)
        project = validated_data.get('project')

        if assigned_to and assigned_to != project.members.all():
            project.members.add(assigned_to)
        return Task.objects.create(**validated_data)