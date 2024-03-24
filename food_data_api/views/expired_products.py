from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator
from food_data_api.models.product import Product
from food_data_api.models.sales import Sale, InventoryAdjustment
from django.db.models import Sum
from dashboard.views.expired_product import (
    get_products_nearing_expiry,
    get_expired_products_by_category,
)
from django.contrib.auth.decorators import login_required
from core.decorators import group_required
from core.helpers.send_email import (
    send_low_inventory_email,
    send_nearing_expiry_email,
    send_expired_product_email,
)
from dashboard.views.notifications import (
    get_low_stock_products,
    get_nearing_expiration_products,
    get_expired_products,
)


def coming_soon(request):
    # Your coming soon view logic here
    return render(request, "coming-soon.html")


@login_required
@group_required
def dashboard_page(request):
    # Ensure the user is authenticated
    if not request.user.is_authenticated:
        return redirect("login")

    # Retrieve necessary data for the stats card
    total_sales = Sale.objects.aggregate(total=Sum("sale_price"))["total"] or 0
    total_inventory_adjustments = (
        InventoryAdjustment.objects.aggregate(total=Sum("adjusted_quantity"))["total"]
        or 0
    )
    low_stock_threshold = 10
    low_stock_items_count = Product.objects.filter(
        stock_quantity__lte=low_stock_threshold
    ).count()
    nearing_expiry_threshold = 30
    nearing_expiry_date = timezone.now().date() + timedelta(
        days=nearing_expiry_threshold
    )
    nearing_expiry_items_count = Product.objects.filter(
        expiry_date__lte=nearing_expiry_date
    ).count()

    # Consider having a function that calculates the average turnover rate
    # average_turnover_rate = get_average_turnover_rate()

    now = timezone.now()
    if now.hour == 22:  # Send emails at 10 PM
        user_email = request.user.email
        user_name = request.user.get_full_name()

        # Retrieve low stock, nearing expiry, and expired products for email notifications
        low_stock_products = get_low_stock_products()
        nearing_expiry_products = get_nearing_expiry_products()
        expired_products = get_expired_products()

        # Send email notifications
        send_low_inventory_email(user_email, user_name, list(low_stock_products))
        for product in nearing_expiry_products:
            send_nearing_expiry_email(user_email, user_name, product)
        for product in expired_products:
            send_expired_product_email(user_email, user_name, product)

        messages.success(request, "Notification emails sent successfully.")

    # Update context with new data for the stats card
    context = {
        "user_name": request.user.get_full_name() or request.user.username,
        "user_group": (
            request.user.groups.first().name
            if request.user.groups.exists()
            else "No Group"
        ),
        "total_sales": total_sales,
        "total_inventory": total_inventory_adjustments,
        "low_stock_items_count": low_stock_items_count,
        "nearing_expiry_items_count": nearing_expiry_items_count,
    }
    return render(request, "index.html", context)


def products_nearing_expiry(request):
    products = get_products_nearing_expiry(request)
    page = request.GET.get("page", 1)
    paginator = Paginator(products, 7)
    try:
        products_page = paginator.page(page)
    except PageNotAnInteger:
        products_page = paginator.page(1)
    except EmptyPage:
        products_page = paginator.page(paginator.num_pages)

    data = list(
        products_page.object_list.values(
            "name", "category__name", "unit_price", "stock_quantity", "expiry_date"
        )
    )

    # Including pagination metadata in the response
    response_data = {
        "data": data,
        "total_pages": paginator.num_pages,
        "current_page": products_page.number,
    }
    return JsonResponse(response_data)


def expired_products_by_category_api(request):
    data = get_expired_products_by_category(request)
    return JsonResponse(data, safe=False)
