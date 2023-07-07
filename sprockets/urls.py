from .views import SprocketsViewSet, FactoryViewSet, SprocketProductionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"factories", FactoryViewSet, basename="factory")
router.register(r"sprockets", SprocketsViewSet, basename="sprocket")
router.register(
    r"sprockets_factory", SprocketProductionViewSet, basename="sprocket_factory"
)
urlpatterns = router.urls
