"""User Model

This model is used to manage the user profile. This model is also used to
create table in database by Django. This model inherits from the AbstractUser.
This is extend-user model. Email is used as username field. Username will be
none in this model. 
"""


from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_user(self, email, password=None, **extra_fields):
    #     """Create and save a regular User with the given email and password."""
    #     extra_fields.setdefault("is_staff", False)
    #     extra_fields.setdefault("is_superuser", False)
    #     return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create Uuperuser
        
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """ User Model

    This is the user model for the blogs_drf app. The user model is used
    to map the user to the database. In this model we extend user with
    followimg fields:
    - email
    - picture
    - address
    - phone number
    And we use other builtin following fields:
    - first_name
    - last_name
    - password
    """

    username = None
    email = models.EmailField(_("email"),
        unique=True, blank=False, null=False
    )
    image = models.ImageField(upload_to="users", blank=True)
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    objects = UserManager()
