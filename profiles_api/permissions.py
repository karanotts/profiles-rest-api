from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Allow users to edit their own data """

    def has_object_permissions(self, request, view, obj):
        """ Check user is trying their own profile """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id # True if logged in user is the user object they're trying to edit