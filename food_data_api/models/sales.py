from django.db import models
from .product import Product
from .region_store import Store, Region


class Sale(models.Model):
    product = models.ForeignKey(Product, related_name="sales", on_delete=models.CASCADE)
    store = models.ForeignKey(Store, related_name="sales", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sale_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )  # This field will now store the calculated sale price
    sale_date = models.DateField()

    def save(self, *args, **kwargs):
        # Calculate the sale_price using the unit_price from the related Product instance
        self.sale_price = self.product.unit_price * self.quantity
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return f"{self.product.name} - ({self.sale_price})"


class InventoryAdjustment(models.Model):
    product = models.ForeignKey(
        Product, related_name="inventory_adjustments", on_delete=models.CASCADE
    )
    adjusted_quantity = models.IntegerField()
    adjustment_date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.product.name}"


class Transaction(models.Model):
    TYPE_CHOICES = [
        ("sale", "Sale"),
        ("return", "Return"),
    ]
    product = models.ForeignKey(
        Product, related_name="transactions", on_delete=models.CASCADE
    )
    transaction_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    quantity = models.PositiveIntegerField()
    transaction_date = models.DateTimeField(auto_now_add=True)
    store = models.ForeignKey(
        Store, related_name="transactions", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Transaction ({self.get_transaction_type_display()}) for {self.product.name}"
