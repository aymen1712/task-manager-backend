from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated

from projects.models import Project
from projects.permissions import IsAdminOrMember
from tasks.models import Task
from tasks.serializers import TaskSerializer


# Create your views here.
class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsAdminOrMember)
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ('title', 'description', 'status', 'priority', 'due_date', 'project', 'assigned_to')
    ordering_fields = ('title', 'priority', 'due_date', 'status')

    def get_queryset(self):
        project_id = self.kwargs['project_pk']
        return Task.objects.filter(project__id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs['project_pk']
        serializer.save(created_by=self.request.user, project_id=project_id)

class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsAdminOrMember)
