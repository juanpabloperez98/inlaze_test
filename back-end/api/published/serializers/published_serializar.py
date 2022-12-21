from rest_framework import serializers
from published.models import Published


class PublishedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Published
        fields = (
            "title",
            "comment",
            "created_at",
            "updated_at"
        )


class PublishedUserSerializer(serializers.ModelSerializer):

    user_nickname = serializers.CharField(source="user.nickname")
    user_names = serializers.CharField(source="user.names")
    user_lastname = serializers.CharField(source="user.lastname")
    user_email = serializers.CharField(source="user.email")
    user_genere = serializers.IntegerField(source="user.genere")

    class Meta:
        model = Published
        fields = (
            "title",
            "comment",
            "user_nickname",
            "user_names",
            "user_lastname",
            "user_email",
            "user_genere",
            "created_at",
            "updated_at"
        )