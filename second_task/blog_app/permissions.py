from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Blog



class CustomPermissionForAdmin(BasePermission):

    def has_permission(self, request, view):

        return bool(request.user.is_superuser)
    

class CustomPermissionForUser(BasePermission):

    def has_permission(self, request, view):

# It is not working as expected

        return bool(Blog.objects.filter(is_public=False))


class AdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
        