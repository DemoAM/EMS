import uuid

from django.db import models

from user.models import User, Role


class ExpanseCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Expanse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    exp_category = models.ForeignKey(ExpanseCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.user.name} , {self.exp_category}"
