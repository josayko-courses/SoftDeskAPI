from rest_framework.serializers import ModelSerializer

from api.models import CustomUser


class UserListSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "first_name", "last_name"]


class UserCreateSerializer(ModelSerializer):
    def create_user(self, email, password, first_name=None, last_name=None):
        """Creates and saves a User with the given email and password."""
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a password")
        user = CustomUser.objects.create(email=email)
        user.first_name = ""
        user.last_name = ""
        if first_name and isinstance(first_name, str):
            user.first_name = first_name
        if last_name and isinstance(last_name, str):
            user.last_name = last_name
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ["id", "email", "password", "first_name", "last_name"]
