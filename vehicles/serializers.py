from rest_framework import serializers
from .models import VehicleStatus, Vehicle

class VehicleStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleStatus
        fields = "__all__"

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"