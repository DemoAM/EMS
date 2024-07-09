from django.contrib import admin
from .models import Organization, EmployeeProfile

# Register your models here.

admin.site.register(Organization)
admin.site.register(EmployeeProfile)
