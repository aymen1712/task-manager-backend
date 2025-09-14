from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from projects.models import Project
from projects.permissions import IsAdminOrOwner, IsAdminOrMember
from projects.serializers import ProjectSerializer


# Create your views here.
class ProjectListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, IsAdminOrMember)
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ('name', 'description')
    ordering_fields = ('name' ,'created_at',)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.role == 'admin':
                return Project.objects.all().distinct()
            return Project.objects.filter(Q(members=user) | Q(created_by=user)).distinct()
        return Project.objects.none()

    def perform_create(self, serializer):
        serializer.save()

class ProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, IsAdminOrOwner)
    lookup_field = 'pk'

