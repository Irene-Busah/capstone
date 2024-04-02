from django.shortcuts import render, redirect
from dashboard.views.authentication import signup_view
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
from core.decorators import group_required
import json
from core.emails.accounts.emails import send_login_successful_email
from food_data_api.views.analysis import get_sales_and_consumption_insights_data
from dashboard.views.analysis import generate_data_analysis, generate_suggestions
from core.helpers.send_email import send_analysis_and_suggestions_email
from food_data_api.views.analysis import insights_and_suggestions_api


def signUp_page(request):
    return render(request, "signup.html")


def signup_api(request):
    signup_view(request)
    return redirect("index")


def login_api(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Get insights and suggestions data
            insights_data = insights_and_suggestions_api(request)
            response = json.loads(insights_data.content.decode("utf-8"))
            analysis = response["analysis"]
            suggestions = response["suggestions"]

            # Send analysis and suggestions email
            send_analysis_and_suggestions_email(
                recipient_email=request.user.email,
                recipient_name=request.user.first_name,
                analysis=analysis,
                suggestions=suggestions,
            )

            return redirect("index")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login")
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")
