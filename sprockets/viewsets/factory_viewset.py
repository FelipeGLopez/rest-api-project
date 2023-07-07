from ..models.factory import Factory
from ..serializers.factory_serializer import FactorySerializer
from .generics import RetrieveViewSet


class FactoryViewSet(RetrieveViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
