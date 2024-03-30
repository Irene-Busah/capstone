from django.db.models import Sum, Avg, F, FloatField, ExpressionWrapper, Q
from django.db.models.functions import Coalesce
from datetime import datetime, timedelta
from food_data_api.models.sales import Sale, InventoryAdjustment
from food_data_api.models.product import Product
from django.utils import timezone
from django.db.models import FloatField
from django.db.models.functions import Cast


def get_inventory_and_purchase_rate_by_category():
    start_of_year = timezone.now().replace(
        month=1, day=1, hour=0, minute=0, second=0, microsecond=0
    )

    # Aggregate sales data by category for the current year
    sales_agg = (
        Sale.objects.filter(sale_date__gte=start_of_year)
        .values("product__category__name")
        .annotate(
            total_sales_quantity=Sum("quantity"),
            cogs_approx=Sum(
                Cast("quantity", FloatField()) * F("product__unit_price"),
                output_field=FloatField(),
            ),
        )
    )

    rates_by_category = {}

    for sale in sales_agg:
        category_name = sale["product__category__name"]

        # Purchase Rate: Total sales quantity for the current year
        purchase_rate = sale["total_sales_quantity"]

        # Average Inventory: Use the average stock_quantity from the Product model for the current category
        average_inventory = Product.objects.filter(
            category__name=category_name
        ).aggregate(
            avg_stock=Coalesce(
                Avg(
                    Cast("stock_quantity", FloatField()),
                    output_field=FloatField(),
                ),
                0,
                output_field=FloatField(),
            )
        )[
            "avg_stock"
        ]

        # Inventory Turnover Rate: COGS approximation divided by average inventory
        turnover_rate = (
            sale["cogs_approx"] / average_inventory if average_inventory else 0
        )

        rates_by_category[category_name] = {
            "turnover_rate": turnover_rate,
            "purchase_rate": purchase_rate,
        }
    print(rates_by_category)
    return rates_by_category
