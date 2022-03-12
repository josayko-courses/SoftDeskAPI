from rest_framework.serializers import ModelSerializer

from api.models import CustomUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["user_id", "email", "first_name", "last_name"]
