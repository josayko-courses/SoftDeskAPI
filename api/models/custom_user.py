from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Custom user model
    """

    username = None
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField("email address", unique=True)
    first_name = models.CharField("first name", max_length=128, blank=True)
    last_name = models.CharField("last name", max_length=128, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
