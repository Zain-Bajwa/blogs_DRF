"""User Model

This model is used to manage the user profile. This model is also used to
create table in database by Django. This model inherits from the AbstractUser.
This is extend-user model. Email is used as username field. Username will be
none in this model.
"""


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from authentication.manager import UserManager


class User(AbstractUser):
    """User Model

    This is the user model for the blogs_drf app. The user model is used
    to map the user to the database.
    """

    username = None
    email = models.EmailField(_("email"), unique=True, blank=False, null=False)
    image = models.ImageField(upload_to="users", blank=True)
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    objects = UserManager()
