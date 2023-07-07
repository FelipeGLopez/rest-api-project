from models.sprocket import Sprocket
from rest_framework import serializers


class SprocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprocket
        fields = ("id", "outside_diameter", "pitch_diameter", "pitch", "teeth")
