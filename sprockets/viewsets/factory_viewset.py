from .generics import RetrieveViewSet
from ..models.factory import Factory
from ..serializers.factory_serializer import FactorySerializer


class FactoryViewSet(RetrieveViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
