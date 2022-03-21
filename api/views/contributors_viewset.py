from rest_framework.viewsets import ModelViewSet

from api.models import Contributor
from api.serializers import ContributorSerializer


class ContributorsViewset(ModelViewSet):
    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.all()
