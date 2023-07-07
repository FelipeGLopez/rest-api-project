from .generics import RetrieveViewSet
from sprockets.models import SprocketProduction
from sprockets.serializers import SprocketProductionSerializer


class SprocketProductionViewSet(RetrieveViewSet):
    queryset = SprocketProduction.objects.all()
    serializer_class = SprocketProductionSerializer
