from rest_framework import viewsets
from team.models import Team
from team.serializers import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    def get_queryset(self):
        queryset = Team.objects.filter(users__contains=request.user)
        return queryset
