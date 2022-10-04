"""Serializers for the authentication Application

This file contains all the serializers for the authentication Application. The
RegisterSerializers is used to create the user.
"""

from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from authentication.models import User


# pylint: disable=too-few-public-methods
class UserRegisterSerializer(serializers.ModelSerializer):
    """User Register Serializer

    In this class we override the method creat to create extend user. The user
    is created using the create method from the User model. The password is set
    using the set_password method from the User model to encrypt the password.
    The user is saved using the save method and returned.`
    """

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        """Meta class for the User Register Serializer"""

        model = User
        fields = ["id", "email", "password", "confirm_password"]
        read_only = ["confirm_password"]

    def validate(self, attrs):
        """Validate the password and confirm password

        This method is used to validate the password and confirm password. If
        the password and confirm password are not same then raise an error.
        This method is also used to validate the weak password. If the password
        is weak then raise an error.
        """

        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        """Create the user

        This method is used to create the user. The user is created using the
        create method from the User model. The password is set using the
        set_password method from the User model to encrypt the password. The
        user is saved using the save method and returned. The user is also
        saved in the database.
        """

        user = User.objects.create(email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()
        return user
