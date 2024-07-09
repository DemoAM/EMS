from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class Role(models.Model):
    class Roles(models.TextChoices):
        ADMIN = "admin", "Admin"
        EMPLOYEE = "employee", "Employee"


class User(AbstractUser):

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    last_login = models.DateTimeField(auto_now=True)
    role = models.CharField(choices=Role.Roles.choices, max_length=20)
    org_name = models.ForeignKey(
        "organization.Organization",
        on_delete=models.CASCADE,
        related_name="org_users",
        null=True,
        blank=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "username"]

    def __str__(self):
        return self.name
