from django.db import models
import uuid
from .category import Category
from .people import Supplier


class Product(models.Model):
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        "Category", related_name="products", on_delete=models.CASCADE
    )
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    reorder_threshold = models.PositiveIntegerField(default=10)
    reorder_amount = models.PositiveIntegerField(default=20)
    expiry_date = models.DateField()
    production_date = models.DateField()
    batch_number = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    supplier = models.ForeignKey(
        "Supplier", related_name="products", on_delete=models.SET_NULL, null=True
    )
    notification_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} (Batch: {self.batch_number})"
