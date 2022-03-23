from django.db import models
from .custom_user import CustomUser


class Project(models.Model):
    """
    Projects
    """

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    class Type(models.TextChoices):
        BACK = "back-end"
        FRONT = "front-end"
        IOS = "iOS"
        ANDROID = "Android"

    type = models.CharField(max_length=64, choices=Type.choices, default=Type.BACK)
    author = models.ForeignKey(
        to=CustomUser, related_name="projects", on_delete=models.CASCADE
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
