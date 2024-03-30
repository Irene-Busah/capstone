from django.db.models import Sum
from food_data_api.models.region_store import Region, Store
from food_data_api.models.sales import Sale


def get_frequently_consumed_by_region(request):
    sales_by_region_and_category = (
        Sale.objects.select_related("product__category", "store__region")
        .values("store__region__name", "product__category__name")
        .annotate(total_quantity=Sum("quantity"))
        .order_by("store__region__name", "-total_quantity")
    )

    # Reorganize data structure
    organized_data = {}
    for item in sales_by_region_and_category:
        category = item["product__category__name"]
        region = item["store__region__name"]
        total_quantity = item["total_quantity"]

        if category not in organized_data:
            organized_data[category] = []

        organized_data[category].append(
            {"region": region, "total_quantity": total_quantity}
        )
    # print(organized_data)
    return organized_data
