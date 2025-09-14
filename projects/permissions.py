from rest_framework import permissions


class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.role == 'admin':
            return True

        return obj.created_by == request.user

class IsAdminOrMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True
        if request.method == 'DELETE':
            return obj.created_by == request.user
        return request.user in obj.members.all()