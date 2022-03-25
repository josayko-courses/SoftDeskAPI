from rest_framework.serializers import ModelSerializer

from api.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "description", "created_time", "author", "issue"]
