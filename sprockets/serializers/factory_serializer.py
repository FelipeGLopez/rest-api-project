from ..models.factory import Factory
from rest_framework import serializers


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = ("id", "name")
