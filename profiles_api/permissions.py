from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Allow users to edit their own user data """

    def has_object_permissions(self, request, view, obj):
        """ Check user is trying to update their own profile """
        if request.method in permissions.SAFE_METHODS:
            return True

        return (
            obj.id == request.user.id
        )  # True if logged in user is the user object they're trying to edit


class UpdateOwnStatus(permissions.BasePermission):
    """ Allow users to edit their own status """

    def has_object_permission(self, request, view, obj):
        """ Check user is trying to update their own status """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
