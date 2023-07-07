from .generics import CreateUpdateRetrieveViewSet
from ..models.sprocket import Sprocket
from ..serializers.sprocket_serializer import SprocketSerializer


class SprocketsViewSet(CreateUpdateRetrieveViewSet):
    queryset = Sprocket.objects.all()
    serializer_class = SprocketSerializer
