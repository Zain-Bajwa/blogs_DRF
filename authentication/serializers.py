"""Serializers for the authentication Application

This file contains all the serializers for the authentication Application. The
RegisterSerializers is used to create the user. The UserViewSerializer is used
to format the user profile data into json format.
"""

from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from authentication.models import User


# pylint: disable=too-few-public-methods
class UserRegisterSerializer(serializers.ModelSerializer):
    """User Register Serializer

    In this class we override the method create to create extend user. The user
    is created using the create method from the User model.
    """

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        """Meta class for the User Register Serializer"""

        model = User
        fields = ["id", "email", "first_name", "last_name", "password"]

    def create(self, validated_data):
        """Create the user

        This method is used to create the user. The user is created using the
        create method from the User model.
        """

        user = User.objects.create_user(**validated_data)
        user.save()
        return user


# pylint: disable=abstract-method
class UserViewSerializer(serializers.ModelSerializer):
    """User View Serializer

    This class is used to format the user data. The user data is returned in a
    json format including the user id, email, first name, last name,
    address, image and phone number.
    """

    class Meta:
        """Meta class for the User View Serializer"""

        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "address",
            "phone_no",
            "image",
        ]
