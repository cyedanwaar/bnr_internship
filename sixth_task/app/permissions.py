from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        # obj.owner is field that will be connected with the user from the projectdashboard and projectmanagerscreen
        # is_internal_user is for giving access to all info to internal users

        # user can only see his own created information
        if request.method in SAFE_METHODS:
            return obj.owner == request.user
        
        return obj.owner == request.user or request.user.is_staff or request.user.is_internal_user
