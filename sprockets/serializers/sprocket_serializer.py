from rest_framework import serializers

from ..models.sprocket import Sprocket


class SprocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprocket
        fields = ("id", "outside_diameter", "pitch_diameter", "pitch", "teeth")
