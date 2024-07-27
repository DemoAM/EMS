from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import EmployeeView
from .views import (
    RegisterView,
    LoginView,
    UserProfile,
    UserChangePasswordView,
    SendPasswordResetEmail,
    UserResetPasswordView,
)


router = DefaultRouter()
router.register("profile", UserProfile, basename="profile")



urlpatterns = [
    path("api/", include(router.urls)),
    path("api/employee/",EmployeeView.as_view(),name="employee"),
    path("api/login/", LoginView.as_view()),
    path("api/register/", RegisterView.as_view(),name="register"),
    # path("api/profile/", UserProfile.as_view(), name="profile"),
    path("api/change/", UserChangePasswordView.as_view(), name="change password"),
    path(
        "api/email-rest-password/",
        SendPasswordResetEmail.as_view(),
        name="send_password_reset_email",
    ),
    path(
        "api/reset-password/<uid>/<token>/",
        UserResetPasswordView.as_view(),
        name="reset_password",
    ),
]
