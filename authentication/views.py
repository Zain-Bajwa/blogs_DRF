""" All Views of the Authentication Application

This file contains all the views of the authentication Application. The views
are used to create, update, delete and list the users.

"""

# pylint: disable=no-member,too-many-ancestors
from rest_framework import generics, status
from rest_framework.response import Response
from authentication.serializers import UserRegisterSerializer


class UserRegisterView(generics.GenericAPIView):
    """User Registration View

    This view is used to create a new user. The user is created using the
    GenericAPIView class. The serializer is used to validate the data. The user
    is created and the data is returned.
    """

    serializer_class = UserRegisterSerializer

    def post(self, request):
        """Create the user"""

        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)
