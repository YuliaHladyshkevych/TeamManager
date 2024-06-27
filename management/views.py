from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from management.models import Team, Person
from management.serializers import TeamSerializer, PersonSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @action(detail=True, methods=["get"])
    def members(self, request, pk=None):
        team = self.get_object()
        members = team.members.all()
        serializer = PersonSerializer(members, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def add_member(self, request, pk=None):
        team = self.get_object()
        person_id = request.data.get("person_id")
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            raise ValidationError("Person not found")
        team.members.add(person)
        return Response({"status": "Member added"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["get"])
    def filter_members(self, request, pk=None):
        team = self.get_object()
        first_name = request.query_params.get("first_name")
        last_name = request.query_params.get("last_name")
        members = team.members.all()
        if first_name:
            members = members.filter(first_name=first_name)
        if last_name:
            members = members.filter(last_name=last_name)
        serializer = PersonSerializer(members, many=True)
        return Response(serializer.data)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    @action(detail=False, methods=["get"])
    def filter_persons(self, request):
        first_name = request.query_params.get("first_name")
        last_name = request.query_params.get("last_name")
        members = Person.objects.all()
        if first_name:
            members = members.filter(first_name=first_name)
        if last_name:
            members = members.filter(last_name=last_name)
        serializer = PersonSerializer(members, many=True)
        return Response(serializer.data)
