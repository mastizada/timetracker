from rest_framework import serializers
from project.models import Project
from timelog.models import TimeLog
from django.db.models import Sum


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for project"""
    total_duration = serializers.SerializerMethodField('get_duration')
    class Meta:
        model = Project
        fields = ('id', 'name', 'customer', 'total_duration', 'modified_at', 'created_at',)

    def get_duration(self, project):
        """
        Get work duration for current project
        """
        return TimeLog.objects.filter(project=project).aggregate(Sum('duration'))['duration__sum']
