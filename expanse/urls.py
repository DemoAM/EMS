from django.urls import path, include
from rest_framework import routers
from .views import ExpanseViewSet

router = routers.DefaultRouter()
router.register(r"expanse", ExpanseViewSet, basename="expanse")


urlpatterns = [
    path("api/", include(router.urls)),
]
