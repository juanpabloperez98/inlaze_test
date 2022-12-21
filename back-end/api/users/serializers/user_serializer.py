from rest_framework import serializers
from users.models import User


class UserdSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "nickname",
            "names",
            "lastname",
            "email",
            "genere"
        )