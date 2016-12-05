from rest_framework import serializers
from project.models import Project
from timelog.models import TimeLog
from django.db.models import Sum


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for project"""
    total_duration = serializers.SerializerMethodField('get_duration')
    customer = serializers.HyperlinkedRelatedField(
        view_name='customer-detail',
        read_only=True
    )
    team = serializers.HyperlinkedRelatedField(
        view_name='team-detail',
        read_only=True
    )

    class Meta:
        model = Project
        fields = ('id', 'name', 'customer', 'team', 'rate', 'total_duration',
                  'modified_at', 'created_at',)

    def get_duration(self, project):
        """Get work duration for current project."""
        return TimeLog.objects.filter(project=project).aggregate(
                Sum('duration'))['duration__sum']
