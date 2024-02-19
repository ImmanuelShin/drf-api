from rest_framework import serializers
from .models import DRF

class DRFSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'name', 'description', 'rating', 'created_at')
        model = DRF