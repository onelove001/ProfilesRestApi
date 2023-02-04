from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allows user edit their profile"""

    def has_object_permission(self, request, view, obj):
        """ Checks for profile of the request user """

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id