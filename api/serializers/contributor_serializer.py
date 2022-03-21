from rest_framework.serializers import ModelSerializer

from api.models import Contributor


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["user", "project", "permission", "role"]
