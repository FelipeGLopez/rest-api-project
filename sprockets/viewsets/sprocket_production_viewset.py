from ..models.sprocket_production import SprocketProduction
from ..serializers.sprocket_production_serializer import \
    SprocketProductionSerializer
from .generics import RetrieveViewSet


class SprocketProductionViewSet(RetrieveViewSet):
    queryset = SprocketProduction.objects.all()
    serializer_class = SprocketProductionSerializer
