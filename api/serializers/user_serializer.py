from rest_framework.serializers import ModelSerializer

from api.models import CustomUser


class UserListSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email"]


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "first_name", "last_name"]
