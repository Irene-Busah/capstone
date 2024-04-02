from django.http import JsonResponse
from dashboard.views.analysis import generate_data_analysis, generate_suggestions
import datetime
from django.db.models import Sum, Avg, Count
from food_data_api.models.sales import Sale, InventoryAdjustment
from food_data_api.models.product import Product
import json


def get_sales_and_consumption_insights_data():
    # Get the current year
    current_year = datetime.datetime.now().year

    # Retrieve sales trends by category for the current year
    sales_trends_data = (
        Sale.objects.filter(sale_date__year=current_year)
        .values("product__category__name")
        .annotate(total_sales=Sum("quantity"), total_revenue=Sum("sale_price"))
        .order_by("-total_sales")
    )

    purchase_trends_data = (
        Sale.objects.filter(sale_date__year=current_year)
        .values("product__category__name")
        .annotate(
            total_purchases=Count("id"),
            avg_product_quantity=Avg("product__stock_quantity"),
        )
        .order_by("-total_purchases")
    )

    # Convert QuerySets to lists and Decimal to float
    sales_trends_data_list = [
        {**item, "total_revenue": float(item["total_revenue"])}
        for item in sales_trends_data
    ]
    purchase_trends_data_list = [
        {**item, "avg_product_quantity": float(item["avg_product_quantity"])}
        for item in purchase_trends_data
    ]

    # Prepare the data dictionary
    insights_data = {
        "sales_trends_data": sales_trends_data_list,
        "purchase_trends_data": purchase_trends_data_list,
    }

    return insights_data


def insights_and_suggestions_api(request):
    # Retrieve the sales and consumption insights data
    insights_data = get_sales_and_consumption_insights_data()

    # Convert the insights data to a string for OpenAI prompt
    data_str = json.dumps(insights_data, indent=2)

    # Generate analysis and suggestions using OpenAI
    analysis = generate_data_analysis(data_str)
    suggestions = generate_suggestions(data_str)

    # Return the analysis and suggestions as a JSON response
    return JsonResponse({"analysis": analysis, "suggestions": suggestions})
