from rest_framework import serializers

from api.models import Contributor

from .user_serializer import UserListSerializer


class ContributorListSerializer(serializers.ModelSerializer):
    def validate(self, data):
        user = data.get("user")
        project = data.get("project")
        if Contributor.objects.filter(user=user, project=project).exists():
            raise serializers.ValidationError("This contributor already exists")
        return super().validate(data)

    class Meta:
        model = Contributor
        fields = ["user", "project", "role"]


class ContributorDetailSerializer(serializers.ModelSerializer):
    def validate(self, data):
        user = data.get("user")
        project = data.get("project")
        if Contributor.objects.filter(user=user, project=project).exists():
            raise serializers.ValidationError("This contributor already exists")
        return super().validate(data)

    user = UserListSerializer()

    class Meta:
        model = Contributor
        fields = ["user", "project", "permission", "role"]
