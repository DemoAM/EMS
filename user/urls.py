from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import SignUpView, UpdateUserView, EmployeeUserViewSet
from .views import LoginAPIView


router = DefaultRouter()
router.register("signup", SignUpView, basename="logup")
router.register("update", UpdateUserView, basename="update")
router.register("employee", EmployeeUserViewSet, basename="employee")
router.register("login", LoginAPIView, basename="login")


urlpatterns = [
    path("api/", include(router.urls)),
]
