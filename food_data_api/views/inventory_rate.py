from django.http import JsonResponse
from dashboard.views.inventory_rate import get_inventory_and_purchase_rate_by_category


def inventory_and_purchase_rate_api(request):
    rates_by_category = get_inventory_and_purchase_rate_by_category()

    return JsonResponse(rates_by_category, safe=False)
