from rest_framework import permissions

class IsUserOrNotAllowed(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else :
            return bool(request.user or request.user.is_authenticated)