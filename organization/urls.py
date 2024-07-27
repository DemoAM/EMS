from django.urls import path, include
from rest_framework import routers

from organization import views
from .dashboard import DashboardView
from .admin_dashboard import AdminDashboardView

router = routers.DefaultRouter()
router.register(r"organization", views.OrganizationViewSet, basename="organization")
router.register("dashboard", DashboardView, basename="dashboard")
urlpatterns = [
    path("api/", include(router.urls)),
    path('api/admin-dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('api/admin-dashboard/<int:id>/', AdminDashboardView.as_view(), name='admin-dashboard-detail'),
]
