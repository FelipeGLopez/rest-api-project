from rest_framework.routers import DefaultRouter

from .viewsets.factory_viewset import FactoryViewSet
from .viewsets.sprocket_production_viewset import SprocketProductionViewSet
from .viewsets.sprocket_viewset import SprocketsViewSet

router = DefaultRouter()
router.register(r"factories", FactoryViewSet, basename="factory")
router.register(r"sprockets", SprocketsViewSet, basename="sprocket")
router.register(
    r"sprockets_factory", SprocketProductionViewSet, basename="sprocket_factory"
)
urlpatterns = router.urls
