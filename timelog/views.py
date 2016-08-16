from rest_framework import viewsets
from timelog.models import TimeLog
from timelog.serializers import TimeLogSerializer


class TimeLogViewSet(viewsets.ModelViewSet):
    queryset = TimeLog.objects.all()
    serializer_class = TimeLogSerializer
