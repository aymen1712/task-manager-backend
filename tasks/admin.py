from django.contrib import admin

from tasks.models import Task


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('project', 'title', 'status', 'created_by', 'assigned_to', 'due_date', 'priority')
    list_filter = ('project', 'status', 'due_date', 'priority', 'assigned_to')
    search_fields = ('title', 'description', 'assigned_to__username', 'created_by__username')
    readonly_fields = ('created_at',)
