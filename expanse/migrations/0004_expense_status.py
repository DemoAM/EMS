# Generated by Django 5.0.7 on 2024-07-26 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expanse", "0003_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="expense",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Approved", "Approved"),
                    ("Rejected", "Rejected"),
                ],
                default="Pending",
                max_length=10,
            ),
        ),
    ]
