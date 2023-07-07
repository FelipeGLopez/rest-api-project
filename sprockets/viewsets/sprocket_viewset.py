from sprockets.models.sprocket import Sprocket
from sprockets.serializers.sprocket_serializer import SprocketSerializer

from .generics import CreateUpdateRetrieveViewSet


class SprocketsViewSet(CreateUpdateRetrieveViewSet):
    queryset = Sprocket.objects.all()
    serializer_class = SprocketSerializer
