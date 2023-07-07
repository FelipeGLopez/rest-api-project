from rest_framework import serializers
from .models import Factory, Sprocket, SprocketProduction


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = ("id", "name")


class SprocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprocket
        fields = ("id", "outside_diameter", "pitch_diameter", "pitch", "teeth")


class SprocketProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SprocketProduction
        fields = ("id", "actual", "goal", "datetime_produced", "factory", "sprocket")
