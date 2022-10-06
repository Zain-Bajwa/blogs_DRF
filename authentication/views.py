""" All Views of the Authentication Application

This file contains all the views of the authentication Application. The views
are used to create, update, delete and list the users. This file also contains
a custom permission class that is used to check if the user is related to the
that Toekn. It also has views for JWT Token creation.

"""

# pylint: disable=no-member,too-many-ancestors
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from authentication.serializers import (
    UserRegisterSerializer, UserViewSerializer
)
from authentication.permissions import OwnProfilePermission
from authentication.models import User


class UserViewSet(
    viewsets.GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    """User ViewSet
    This viewset is used to retrieve, update and delete a user. In this class
    JWT authentication is used to authenticate the user. This class also uses
    the OwnProfilePermission class to check if the user is related to his
    token.
    """

    queryset = User.objects.all()

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, OwnProfilePermission]
    serializer_class = UserViewSerializer
    lookup_field = "pk"

    def destroy(self, request, *args, **kwargs):
        """Inactivate the user"""
        return Response(
            User.objects.filter(pk=kwargs["pk"]).update(is_active=False),
            status=status.HTTP_204_NO_CONTENT,
        )

    def get_serializer_class(self):
        """Use UserRegisterSerializer if the request is POST"""
        if self.action == "create":
            return UserRegisterSerializer
        return self.serializer_class
