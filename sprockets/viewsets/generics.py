from rest_framework import mixins, viewsets


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


class ListViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    pass
