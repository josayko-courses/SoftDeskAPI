from rest_framework.serializers import ModelSerializer

from api.models import Project, Contributor
from .contributor_serializer import ContributorSerializer


class ProjectListSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "title", "description", "type"]


class ProjectDetailSerializer(ModelSerializer):
    users = ContributorSerializer(many=True)

    class Meta:
        model = Project
        fields = ["id", "title", "description", "type", "users"]
