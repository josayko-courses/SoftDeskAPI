from rest_framework.serializers import ModelSerializer

from api.models import Comment
from .user_serializer import UserListSerializer
from .issue_serializer import IssueSerializer


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "description", "created_time", "author", "issue"]
