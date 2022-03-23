from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator

from api.models import Contributor

from .user_serializer import UserDetailSerializer


class ContributorListSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["user", "project", "role"]
        validators = [
            UniqueTogetherValidator(
                queryset=Contributor.objects.all(), fields=["user", "project"]
            )
        ]


class ContributorDetailSerializer(ModelSerializer):
    user = UserDetailSerializer()

    class Meta:
        model = Contributor
        fields = ["user", "project", "permission", "role"]
        validators = [
            UniqueTogetherValidator(
                queryset=Contributor.objects.all(), fields=["user", "project"]
            )
        ]
