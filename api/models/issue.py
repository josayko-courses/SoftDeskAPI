import uuid
from django.db import models
from .custom_user import CustomUser


class Issue(models.Model):
    """
    Issues
    """

    issue_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=256)
    tag = models.CharField(max_length=64)
    priority = models.CharField(max_length=64)
    status = models.CharField(max_length=64)
    created_time = models.DateTimeField(auto_now_add=True)

    # Relations
    # MANY issues to ONE author (user)
    author = models.ForeignKey(
        to=CustomUser, on_delete=models.CASCADE, related_name="issues"
    )

    # MANY issues to ONE assignee (user)
    assignee = models.ForeignKey(
        to=CustomUser, on_delete=models.SET_NULL, null=True, related_name="assignee"
    )
