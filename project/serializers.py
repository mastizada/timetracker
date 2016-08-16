from rest_framework import serializers
from project.models import Project
from timelog.models import TimeLog

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
        duration = 0
        timelogs = TimeLog.objects.filter(project=project)
        for timelog in timelogs:
            if timelog.duration:
                duration += timelog.duration
        return duration
