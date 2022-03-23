from django.db import models

from .custom_user import CustomUser
from .project import Project


class Contributor(models.Model):
    """
    Contributor through model is equivalent to a many-to-many relationship between
    users and projects
    """

    user = models.ForeignKey(
        to=CustomUser, on_delete=models.CASCADE, related_name="contributions"
    )
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name="users"
    )

    class Permission(models.TextChoices):
        RDONLY = "RDONLY", "Read-only"
        RDWR = "RDWR", "Read and write"

    permission = models.CharField(
        max_length=6, choices=Permission.choices, default=Permission.RDONLY
    )
    role = models.CharField(max_length=64)

    class Meta:
        unique_together = (
            "user",
            "project",
        )
