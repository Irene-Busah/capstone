from datetime import datetime, timedelta
from food_data_api.models.product import Product
from django.utils import timezone


def get_notification_data(request):
    low_stock_threshold = 10
    soon_to_expire_threshold = 30

    low_stock_items = Product.objects.filter(stock_quantity__lte=low_stock_threshold)
    soon_to_expire_items = Product.objects.filter(
        expiry_date__lte=timezone.now().date()
        + timezone.timedelta(days=soon_to_expire_threshold),
        expiry_date__gt=timezone.now().date(),
    )
    expired_items = Product.objects.filter(expiry_date__lte=timezone.now().date())

    data = {
        "low_stock_items": low_stock_items,
        "soon_to_expire_items": soon_to_expire_items,
        "expired_items": expired_items,
    }

    return data


def get_low_stock_products():
    low_stock_threshold = 10
    return Product.objects.filter(stock_quantity__lte=low_stock_threshold)


def get_nearing_expiration_products():
    nearing_expiration_threshold = datetime.today() + timedelta(days=30)
    return Product.objects.filter(expiry_date__lte=nearing_expiration_threshold)


def get_expired_products():
    return Product.objects.filter(expiry_date__lt=datetime.today())
