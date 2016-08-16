from rest_framework import serializers
from project.models import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'customer', 'modified_at', 'created_at',)
