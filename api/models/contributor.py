from django.db import models

from .custom_user import CustomUser
from .project import Project


class Contributor(models.Model):
    """
    Contributor through model is equivalent to a many-to-many relationship between
    users and projects
    """

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        to=CustomUser, on_delete=models.CASCADE, related_name="contributions"
    )
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name="users"
    )

    class Permission(models.TextChoices):
        ROOT = "Root"
        GROUP = "Group"
        USER = "User"

    permission = models.CharField(
        max_length=64, choices=Permission.choices, default=Permission.USER
    )

    class Role(models.TextChoices):
        AUTHOR = "Author"
        CONTRIB = "Contributor"

    role = models.CharField(max_length=64, choices=Role.choices, default=Role.CONTRIB)

    class Meta:
        unique_together = (
            "user",
            "project",
        )
