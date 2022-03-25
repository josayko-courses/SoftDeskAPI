from rest_framework import serializers

from api.models import Project

from .contributor_serializer import ContributorDetailSerializer


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "title", "description", "type", "author"]


class ProjectDetailSerializer(serializers.ModelSerializer):
    users = ContributorDetailSerializer(many=True)

    class Meta:
        model = Project
        fields = ("id", "title", "description", "type", "author", "users")
