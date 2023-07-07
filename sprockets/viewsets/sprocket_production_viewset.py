from sprockets.models.sprocket_production import SprocketProduction
from sprockets.serializers.sprocket_production_serializer import (
    SprocketProductionSerializer,
)

from .generics import ListViewSet


class SprocketProductionViewSet(ListViewSet):
    queryset = SprocketProduction.objects.all()
    serializer_class = SprocketProductionSerializer
