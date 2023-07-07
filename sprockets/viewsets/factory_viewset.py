from sprockets.models.factory import Factory
from sprockets.serializers.factory_serializer import FactorySerializer

from .generics import RetrieveViewSet


class FactoryViewSet(RetrieveViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
