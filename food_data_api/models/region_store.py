from django.db import models
import uuid

class Region(models.Model):
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Store(models.Model):
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=500)
    region = models.ForeignKey(Region, related_name='stores', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
