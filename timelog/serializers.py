from rest_framework import serializers
from timelog.models import TimeLog

class TimeLogSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for timelog."""
    name = serializers.SerializerMethodField('get_title')
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        read_only=True
    )
    project = serializers.HyperlinkedRelatedField(
        view_name='project-detail',
        read_only=True
    )

    class Meta:
        model = TimeLog
        fields = (
            'id', 'name', 'started_at', 'ended_at', 'duration', 'user', 'project',
        )

    def get_title(self, timelog):
        """
        Get custom title
        """
        return timelog.__str__()
