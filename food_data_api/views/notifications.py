from django.shortcuts import render
from django.http import JsonResponse
from dashboard.views.notifications import get_notification_data
from simulate_data import update_existing_products_notification_time
from core.helpers.send_email import (
    send_low_inventory_email,
    send_expired_product_email,
    send_nearing_expiry_email,
)
from datetime import datetime


def notification_page(request):
    user = request.user
    user_name = request.user.get_full_name() or request.user.username

    user_group = (
        request.user.groups.first().name if request.user.groups.exists() else "No Group"
    )

    context = {"user_name": user_name, "user_group": user_group, "user": user}
    return render(request, "notification.html", context)


def notifications_api(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Authentication required"}, status=401)

    data = get_notification_data(request)

    # Current server time
    now = datetime.now()

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

    response_data = {
        "low_stock_items": list(
            data["low_stock_items"].values("name", "stock_quantity")
        ),
        "soon_to_expire_items": list(
            data["soon_to_expire_items"].values("name", "expiry_date")
        ),
        "expired_items": list(data["expired_items"].values("name", "expiry_date")),
    }

    return JsonResponse(response_data)
