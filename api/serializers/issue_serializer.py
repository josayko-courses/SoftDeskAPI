from rest_framework.serializers import ModelSerializer

from api.models import Issue
from .user_serializer import UserDetailSerializer


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"
