from ..models.sprocket import Sprocket
from ..serializers.sprocket_serializer import SprocketSerializer
from .generics import CreateUpdateRetrieveViewSet


class SprocketsViewSet(CreateUpdateRetrieveViewSet):
    queryset = Sprocket.objects.all()
    serializer_class = SprocketSerializer
