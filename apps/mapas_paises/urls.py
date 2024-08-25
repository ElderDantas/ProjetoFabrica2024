from django.urls import path, include
from rest_framework import routers
from apps.mapas_paises.api.viewsets import PaisesViewSet

router = routers.DefaultRouter()
router.register(r"paises", PaisesViewSet, basename="pais")
router.register(r"capital", PaisesViewSet, basename="capital")

urlpatterns = [
    path("", include(router.urls))
]
