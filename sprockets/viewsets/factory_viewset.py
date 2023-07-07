from .generics import RetrieveViewSet
from sprockets.models import Factory
from serializers.factory_serializer import FactorySerializer


class FactoryViewSet(RetrieveViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
