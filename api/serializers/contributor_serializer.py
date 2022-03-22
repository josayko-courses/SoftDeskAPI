from rest_framework.serializers import ModelSerializer

from api.models import Contributor
from .user_serializer import UserListSerializer, UserDetailSerializer


class ContributorListSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["user", "role"]


class ContributorDetailSerializer(ModelSerializer):
    user = UserDetailSerializer()

    class Meta:
        model = Contributor
        fields = ["user", "project", "permission", "role"]
