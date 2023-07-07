from .generics import RetrieveViewSet
from sprockets.models import SprocketProduction
from serializers.sprocket_production_serializer import SprocketProductionSerializer


class SprocketProductionViewSet(RetrieveViewSet):
    queryset = SprocketProduction.objects.all()
    serializer_class = SprocketProductionSerializer
