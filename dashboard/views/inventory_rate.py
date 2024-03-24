from django.db.models import Sum, Avg, F, FloatField, ExpressionWrapper, Q
from django.db.models.functions import Coalesce
from datetime import datetime, timedelta
from food_data_api.models.sales import Sale, InventoryAdjustment
from django.utils import timezone


def get_inventory_and_purchase_rate_by_category():
    one_year_ago = timezone.now() - timedelta(days=365)
    today = timezone.now()

    # Calculate total sold for each category over the past year
    sales_agg = (
        Sale.objects.filter(sale_date__gte=one_year_ago, sale_date__lte=today)
        .values("product__category__name")
        .annotate(
            sold_quantity=Sum("quantity"),
            cogs=Sum(
                F("quantity") * F("product__unit_price"), output_field=FloatField()
            ),
        )
    )

    # Calculate net inventory adjustments for each category over the past year
    adjustments_agg = (
        InventoryAdjustment.objects.filter(
            adjustment_date__gte=one_year_ago, adjustment_date__lte=today
        )
        .values("product__category__name")
        .annotate(net_adjustment=Sum("adjusted_quantity"))
    )

    # Combine sales and adjustments to calculate turnover and acquisition rates
    rates_by_category = []
    for sale in sales_agg:
        category_name = sale["product__category__name"]

        # Find matching adjustments
        matching_adjustment = next(
            (
                adj
                for adj in adjustments_agg
                if adj["product__category__name"] == category_name
            ),
            {"net_adjustment": 0},
        )

        # Calculate turnover rate: COGS / Average Inventory
        # For simplicity, let's consider COGS as total sales value and ignore beginning inventory
        average_inventory = (sale["cogs"] + matching_adjustment["net_adjustment"]) / 2
        turnover_rate = sale["cogs"] / average_inventory if average_inventory else 0

        # Acquisition rate: net adjustment quantity (which includes sales as outgoing stock)
        acquisition_rate = matching_adjustment["net_adjustment"]

        rates_by_category.append(
            {
                "category": category_name,
                "turnover_rate": turnover_rate,
                "acquisition_rate": acquisition_rate,
            }
        )

    return rates_by_category
