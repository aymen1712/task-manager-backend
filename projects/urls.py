from django.urls import path

from projects.models import Project
from projects.views import ProjectListCreateAPIView, ProjectDetailAPIView

urlpatterns = [
    path('', ProjectListCreateAPIView.as_view(), name='projects'),
    path('<uuid:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),
]