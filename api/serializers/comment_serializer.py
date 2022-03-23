from rest_framework.serializers import ModelSerializer

from api.models import Comment

from .issue_serializer import IssueSerializer
from .user_serializer import UserListSerializer


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "description", "created_time", "author", "issue"]
