from rest_framework.serializers import ModelSerializer

from api.models import Project

from .contributor_serializer import ContributorDetailSerializer


class ProjectListSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "title", "description", "type"]


class ProjectDetailSerializer(ModelSerializer):
    users = ContributorDetailSerializer(many=True)

    class Meta:
        model = Project
        fields = ["id", "title", "description", "type", "users"]
