from rest_framework import serializers
from models import SprocketProduction


class SprocketProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SprocketProduction
        fields = ("id", "actual", "goal", "datetime_produced", "factory", "sprocket")
