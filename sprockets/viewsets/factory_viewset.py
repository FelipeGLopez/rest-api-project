from .generics import RetrieveViewSet
from sprockets.models import Factory
from sprockets.serializers import FactorySerializer


class FactoryViewSet(RetrieveViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
