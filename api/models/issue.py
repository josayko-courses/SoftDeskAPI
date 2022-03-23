from django.db import models

from .custom_user import CustomUser
from .project import Project


class Issue(models.Model):
    """
    Issues
    """

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    class Tag(models.TextChoices):
        BUG = "Bug"
        IMPROVE = "Improvement"
        TASK = "Task"

    tag = models.CharField(max_length=64, choices=Tag.choices, default=Tag.TASK)

    class Priority(models.TextChoices):
        LOW = "Low"
        MEDIUM = "Medium"
        HIGH = "High"

    priority = models.CharField(
        max_length=64, choices=Priority.choices, default=Priority.MEDIUM
    )

    class Status(models.TextChoices):
        TODO = "To do"
        ONGOING = "Ongoing"
        DONE = "Done"

    status = models.CharField(
        max_length=64, choices=Status.choices, default=Status.TODO
    )
    created_time = models.DateTimeField(auto_now_add=True)

    # Relations
    # MANY issues to ONE project
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name="issues"
    )

    # MANY issues to ONE author (user)
    author = models.ForeignKey(
        to=CustomUser, on_delete=models.CASCADE, related_name="issues"
    )

    # MANY issues to ONE assignee (user)
    assignee = models.ForeignKey(
        to=CustomUser, on_delete=models.SET_NULL, null=True, related_name="assignations"
    )
