from rest_framework import serializers

from accounts.models import User
from projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):

    created_by = serializers.ReadOnlyField(source='created_by.username')

    members = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), required=False)
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'created_at', 'created_by', 'members')
        read_only_fields = ('id', 'created_at')

    def create(self, validated_data):
        created_by = self.context['request'].user
        members_data = validated_data.pop('members', [])
        project = Project.objects.create(created_by=created_by, **validated_data)
        members_data.append(created_by)
        project.members.set(members_data)

        return project
