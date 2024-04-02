from django.db import models
from django.contrib.auth.models import User
import uuid


class NotificationSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    low_inventory = models.BooleanField(default=True)
    nearing_expiry = models.BooleanField(default=True)
    expired_products = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} Notification Settings"


class Supplier(models.Model):
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    contact_info = models.TextField()

    def __str__(self):
        return self.name


# class Customer(models.Model):
#     name = models.CharField(max_length=255, null=True)
#     loyalty_points = models.PositiveIntegerField(default=0)
#     address = models.TextField(blank=True, null=True)
#     phone_number = models.CharField(max_length=20, blank=True, null=True)
#     email = models.EmailField(blank=True, null=True)
#     preferences = models.JSONField(blank=True, null=True)
#     joined_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.name


# FatSecret API
# Client ID: a7c8a70b7f2c4229b36d69c69a6adcbd
# Client Secret: d86a3db155c24038a3f953f96436a0fa
