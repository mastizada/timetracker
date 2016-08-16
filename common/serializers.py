from rest_framework import serializers
from common.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for user."""

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'modified_at', 'created_at',)
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def update(self, user, data=None):
        user.set_password(data['password'])
        user.save()
        return user


class CurrentUserSerializer(UserSerializer):
    """Serializer for current user."""
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'modified_at', 'created_at',)
        extra_kwargs = {
            'password': {'write_only': True}
}
