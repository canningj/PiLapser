from rest_framework import serializers
from .models import timelapseParams


class paramSerializer(serializers.ModelSerializer):
    class Meta:
        model = timelapseParams
        fields = ('total_images', 'length', 'interval', 'shutter_speed', 'direction')