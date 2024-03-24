from django.db.models import Sum, F
from food_data_api.models.sales import Sale

def get_sales_by_category(request):
    sales_by_category = (
        Sale.objects
        .select_related('product__category')
        .values('product__category__name')
        .annotate(total_revenue=Sum(F('quantity') * F('product__unit_price')))
        .order_by('-total_revenue')
    )
    # print(sales_by_category)
    return list(sales_by_category)

# [{'product__category__name': 'Grains', 'total_revenue': Decimal('589674.51')}, {'product__category__name': 'Canned', 'total_revenue': Decimal('58500.00')}, {'product__category__name': 'Beverages', 'total_revenue': Decimal('1575.46')}, {'product__category__name': 'Snacks', 'total_revenue': Decimal('1116.76')}, {'product__category__name': 'Canned Goods', 'total_revenue': Decimal('1008.28')}, {'product__category__name': 'Condiments', 'total_revenue': Decimal('987.11')}]
