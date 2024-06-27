from rest_framework import serializers
from .models import Team, Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "first_name", "last_name", "email", "team"]


class TeamSerializer(serializers.ModelSerializer):
    members = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ["id", "name", "description", "members"]
