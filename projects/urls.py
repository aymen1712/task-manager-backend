from django.urls import path

from projects.models import Project
from projects.views import ProjectListCreateAPIView, ProjectDetailAPIView
from tasks.views import TaskListCreateAPIView, TaskDetailAPIView

urlpatterns = [
    path('', ProjectListCreateAPIView.as_view(), name='projects'),
    path('<uuid:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),
    path('<uuid:project_pk>/tasks/', TaskListCreateAPIView.as_view(), name='tasks'),
    path('<uuid:project_pk>/tasks/<uuid:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
]