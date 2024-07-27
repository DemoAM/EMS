from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()


class Organization(models.Model):
    organization_id = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False
    )
    organization_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=100)
    no_employees = models.IntegerField()
    organization_type = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.organization_name


class EmployeeProfile(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    previous_job = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name
