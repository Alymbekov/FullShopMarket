from rest_framework import permissions
from applications.users.models import Profile



class IsAuthorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff and request.user.is_authenticated
        

    
