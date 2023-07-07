from rest_framework import mixins, viewsets

from sprockets.models import Factory, Sprocket, SprocketProduction
from sprockets.serializers import (
    FactorySerializer,
    SprocketProductionSerializer,
    SprocketSerializer,
)


class CreateUpdateRetrieveViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    pass


class RetrieveViewSet(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    pass


class FactoryViewSet(RetrieveViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class SprocketsViewSet(CreateUpdateRetrieveViewSet):
    queryset = Sprocket.objects.all()
    serializer_class = SprocketSerializer


class SprocketProductionViewSet(RetrieveViewSet):
    queryset = SprocketProduction.objects.all()
    serializer_class = SprocketProductionSerializer
