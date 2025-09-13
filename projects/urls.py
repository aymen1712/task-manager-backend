from django.urls import path

from projects.models import Project
from projects.views import ProjectListCreateAPIView

urlpatterns = [
    path('', ProjectListCreateAPIView.as_view(), name='projects'),
]