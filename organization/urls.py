from django.urls import path, include
from rest_framework import routers

from organization import views
from .dashboard import DashboardView

router = routers.DefaultRouter()
router.register(r"organizations", views.OrganizationViewSet, basename="organization")
router.register("dashboard", DashboardView, basename="dashboard")
urlpatterns = [
    path("api/", include(router.urls)),
]
