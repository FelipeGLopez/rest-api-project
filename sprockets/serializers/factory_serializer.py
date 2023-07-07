from rest_framework import serializers

from sprockets.models.factory import Factory


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = ("id", "name")
