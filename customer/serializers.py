from rest_framework import serializers
from customer.models import Customer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for customers."""
    class Meta:
        model = Customer
        fields = ('id', 'name', 'modified_at', 'created_at',)
