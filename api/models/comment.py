import uuid
from django.db import models
from .custom_user import CustomUser
from .issue import Issue


class Comment(models.Model):
    """
    Comments
    """

    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=256)
    created_time = models.DateTimeField(auto_now_add=True)

    # Relations
    # MANY comments to ONE author (user)
    author = models.ForeignKey(
        to=CustomUser, on_delete=models.CASCADE, related_name="comments"
    )

    # MANY comments to ONE issue
    issue = models.ForeignKey(
        to=Issue, on_delete=models.CASCADE, related_name="comments"
    )
