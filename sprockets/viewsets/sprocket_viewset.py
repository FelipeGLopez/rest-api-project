from .generics import CreateUpdateRetrieveViewSet
from sprockets.models import Sprocket
from sprockets.serializers import SprocketSerializer


class SprocketsViewSet(CreateUpdateRetrieveViewSet):
    queryset = Sprocket.objects.all()
    serializer_class = SprocketSerializer
