from django.contrib import admin

from projects.models import Project


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'created_by')
    list_filter = ('name', 'created_at', 'created_by')
    search_fields = ('name', 'created_by__username', 'created_at')
    ordering = ('-created_at', 'name')

