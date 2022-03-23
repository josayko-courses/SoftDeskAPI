from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError

from api.models import Contributor

from .user_serializer import UserDetailSerializer


class ContributorListSerializer(ModelSerializer):
    def validate(self, data):
        user = data.get("user")
        project = data.get("project")
        if Contributor.objects.filter(user=user, project=project).exists():
            raise ValidationError("This contributor already exists")
        return super().validate(data)

    class Meta:
        model = Contributor
        fields = ["user", "project", "role"]


class ContributorDetailSerializer(ModelSerializer):
    def validate(self, data):
        user = data.get("user")
        project = data.get("project")
        if Contributor.objects.filter(user=user, project=project).exists():
            raise ValidationError("This contributor already exists")
        return super().validate(data)

    user = UserDetailSerializer()

    class Meta:
        model = Contributor
        fields = ["user", "project", "permission", "role"]
