from rest_framework import serializers
from team.models import Team


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for team"""

    class Meta:
        model = Team
        fields = ('id', 'name', 'users', 'modified_at', 'created_at',)
