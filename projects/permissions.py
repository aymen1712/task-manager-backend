from rest_framework import permissions


class IsAdminOrOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.role == 'admin':
            return True

        if request.user and obj.created_by == request.user:
            return True

        return False