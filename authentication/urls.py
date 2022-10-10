"""Authentication Application URL Configuration

This file contains all the URLs of the authentication Application. This file is
used to connect the URLs to the views. The URLs are used to create, update,
delete a user. It is also used to create new tokens, refresh and verify the
tokens.
"""

from django.urls import include, re_path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework import routers
from authentication.views import UserViewSet, CreateTokenView

# pylint: disable=invalid-name
app_name = "authentication"
router = routers.DefaultRouter()

# For retrieve, update, and delete a user
router.register("user", UserViewSet, basename="user-view")

urlpatterns = [
    re_path("", include("djoser.urls")),
    re_path("jwt/create/", CreateTokenView.as_view(), name="create-token"),
    re_path("jwt/refresh/", TokenRefreshView.as_view(), name="refresh-token"),
    re_path("jwt/verify/", TokenVerifyView.as_view(), name="verify-token"),

]

urlpatterns += router.urls
