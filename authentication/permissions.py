"""Authentication Permissions

This file is used to define all permissions of user. This includes permissions
which API user can access.
"""

from rest_framework import permissions
from django.core.exceptions import ObjectDoesNotExist
from authentication.models import User


class OwnProfilePermission(permissions.BasePermission):
    """Custom Permission Class for the UserViewSet class

    This class is used to check if the user is related to his token. This class
    is used in the UserViewSet class. This class is inherited from the
    BasePermission to connect to the has_permission method.
    """

    def has_permission(self, request, view):
        """Check if the user is related to the token"""

        user_id = view.kwargs.get("pk") or view.kwargs.get("user_id")

        try:
            return request.user == User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return False
