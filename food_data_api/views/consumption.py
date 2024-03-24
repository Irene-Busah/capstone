from django.http import JsonResponse
from dashboard.views.consumption import get_frequently_consumed_by_region


def frequently_consumed_by_region_api(request):
    sales_data = get_frequently_consumed_by_region(request)
    return JsonResponse(sales_data, safe=False)
