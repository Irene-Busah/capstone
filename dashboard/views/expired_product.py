from datetime import timedelta
from django.utils import timezone
from food_data_api.models.product import Product
from django.db.models import Count, F, FloatField
from django.db.models.functions import ExtractYear, Now


def get_products_nearing_expiry(request):
    today = timezone.now().date()
    expiry_threshold = today + timedelta(days=30)
    nearing_expiry_products = Product.objects.filter(
        expiry_date__lte=expiry_threshold
    ).order_by("expiry_date")
    return nearing_expiry_products


def get_expired_products_by_category(request):
    yearly_totals = (
        Product.objects.filter(expiry_date__lt=Now())
        .annotate(expiry_year=ExtractYear("expiry_date"))
        .values("expiry_year")
        .annotate(yearly_total=Count("unique_id"))
        .order_by("expiry_year")
    )

    # Convert yearly_totals to a dictionary for easier access
    yearly_totals_dict = {
        item["expiry_year"]: item["yearly_total"] for item in yearly_totals
    }

    # Step 2: Calculate the total and percentage for each category within each year
    expired_products = (
        Product.objects.filter(expiry_date__lt=Now())
        .annotate(expiry_year=ExtractYear("expiry_date"))
        .values("expiry_year", "category__name")
        .annotate(total=Count("unique_id"))
        .order_by("expiry_year", "category__name")
    )

    # Calculate percentage for each category based on the yearly total
    for product in expired_products:
        year_total = yearly_totals_dict.get(product["expiry_year"], 0)
        product["percentage"] = (
            (product["total"] / year_total) * 100 if year_total else 0
        )

    # Organize data by year for easier consumption by the frontend
    data_by_year = {}
    for product in expired_products:
        year = product["expiry_year"]
        if year not in data_by_year:
            data_by_year[year] = []
        data_by_year[year].append(
            {
                "category_name": product["category__name"],
                "total_expired": product["total"],
                "percentage": product["percentage"],
            }
        )

    print(data_by_year)

    return data_by_year
