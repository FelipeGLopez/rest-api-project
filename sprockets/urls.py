from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from .viewsets.factory_viewset import FactoryViewSet
from .viewsets.sprocket_production_viewset import SprocketProductionViewSet
from .viewsets.sprocket_viewset import SprocketsViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Powerflex API",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r"factories", FactoryViewSet, basename="factory")
router.register(r"sprockets", SprocketsViewSet, basename="sprocket")
router.register(
    r"sprockets_factory", SprocketProductionViewSet, basename="sprocket_factory"
)

urlpatterns = router.urls + [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
