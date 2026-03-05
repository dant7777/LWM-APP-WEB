from rest_framework.routers import DefaultRouter
from .views import (
    ContinentViewSet,
    ZoneViewSet,
    CountryViewSet,
    DistrictViewSet,
    AssemblyViewSet,
)

router = DefaultRouter()

router.register("continents", ContinentViewSet)
router.register("zones", ZoneViewSet)
router.register("countries", CountryViewSet)
router.register("districts", DistrictViewSet)
router.register("assemblies", AssemblyViewSet)

urlpatterns = router.urls