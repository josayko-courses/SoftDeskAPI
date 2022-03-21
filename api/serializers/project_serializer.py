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

        def create(self, validated_data):
            users_data = validated_data.pop("users")
            project = Project.objects.create(**validated_data)
            for users_data in users_data:
                Contributor.objects.create(project=project, **users_data)
            return project
