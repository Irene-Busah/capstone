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

    now = timezone.now()
    if now.hour == 7:
        # Convert QuerySet to a list of dictionaries for low stock products
        low_stock_products = [
            {"name": item.name, "stock_quantity": item.stock_quantity}
            for item in data["low_stock_items"]
        ]
        nearing_expiry_products = list(
            data["soon_to_expire_items"].values("name", "expiry_date")
        )
        expired_products = list(data["expired_items"].values("name", "expiry_date"))

        # Send low inventory email if there are any low stock products
        if low_stock_products:
            send_low_inventory_email(
                recipient_email=request.user.email,
                recipient_name=request.user.get_full_name() or request.user.username,
                low_stock_products=low_stock_products,
            )

        if nearing_expiry_products:
            send_nearing_expiry_email(
                recipient_email=request.user.email,
                recipient_name=request.user.get_full_name() or request.user.username,
                nearing_expiry_products=nearing_expiry_products,
            )

        if expired_products:
            send_expired_product_email(
                recipient_email=request.user.email,
                recipient_name=request.user.get_full_name() or request.user.username,
                expired_products=expired_products,
            )

        messages.success(request, "Notification emails sent successfully.")

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
