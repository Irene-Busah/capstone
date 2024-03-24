from django.db.models import Sum
from food_data_api.models.region_store import Region, Store
from food_data_api.models.sales import Sale

def get_frequently_consumed_by_region(request):
    sales_by_region_and_category = (
        Sale.objects
        .select_related('product__category', 'store__region')
        .values('store__region__name', 'product__category__name')
        .annotate(total_quantity=Sum('quantity'))
        .order_by('store__region__name', '-total_quantity')
    )
    print(sales_by_region_and_category)
    return list(sales_by_region_and_category)
