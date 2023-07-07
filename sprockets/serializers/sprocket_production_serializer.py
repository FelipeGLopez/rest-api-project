from ..models.sprocket_production import SprocketProduction
from rest_framework import serializers


class SprocketProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SprocketProduction
        fields = ("id", "actual", "goal", "datetime_produced", "factory", "sprocket")
