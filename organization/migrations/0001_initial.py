# Generated by Django 5.0.7 on 2024-07-26 13:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EmployeeProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("password", models.CharField(blank=True, max_length=100, null=True)),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("previous_job", models.CharField(max_length=100)),
                ("position", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "organization_id",
                    models.UUIDField(
                        default=uuid.uuid1,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("organization_name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("address", models.CharField(max_length=100)),
                ("no_employees", models.IntegerField()),
                ("organization_type", models.CharField(max_length=100)),
            ],
        ),
    ]
