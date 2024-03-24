from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from food_data_api.models.product import Product


@receiver(post_save, sender=Product)
def update_product_notification_time(sender, instance, created, **kwargs):
    if not created:  # Only proceed for existing instances
        low_stock_threshold = 10
        nearing_expiration_days = 30
        now = timezone.now()

        update_required = False

        if instance.stock_quantity <= low_stock_threshold:
            update_required = True

        if (
            instance.expiry_date
            and (instance.expiry_date - now.date()).days <= nearing_expiration_days
        ):
            update_required = True

        if update_required:
            Product.objects.filter(pk=instance.pk).update(notification_time=now)


# update_existing_products_notification_time()
