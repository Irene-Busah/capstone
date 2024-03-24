from django.http import JsonResponse
from dashboard.views.sales import get_sales_by_category


def sales_by_category_api(request):
    sales_data = get_sales_by_category(request)
    return JsonResponse(sales_data, safe=False)
