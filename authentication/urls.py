"""Authentication Application URL Configuration

This file contains all the URLs of the authentication Application. This file is
used to connect the URLs to the views. The URLs are used to create, update,
delete a user. It is also used to create new tokens, refresh and verify the
tokens.
"""

from django.urls import include, re_path

# from django.conf.urls import url
from rest_framework import routers
from authentication.views import UserViewSet

# pylint: disable=invalid-name
app_name = "authentication"
router = routers.DefaultRouter()

# For retrieve, update, and delete a user
router.register("user", UserViewSet, basename="user-view")

urlpatterns = [
    re_path("", include("djoser.urls")),
    re_path("", include("djoser.urls.jwt")),
]

urlpatterns += router.urls
