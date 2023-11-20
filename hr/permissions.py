from rest_framework import permissions


class IsNotRussianEmail(permissions.BasePermission):
    """
    Allows access only to users whose email does not end with .ru
    """

    def has_permission(self, request, view) -> bool:
        if request.user and request.user.email:
            return not request.user.email.endswith('.ru')
        return False