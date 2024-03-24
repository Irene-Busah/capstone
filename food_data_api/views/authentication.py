from django.shortcuts import render, redirect
from dashboard.views.authentication import signup_view
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
from core.decorators import group_required


# def login_page(request):
#     return render(request, "login.html")


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
            return redirect("index")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login")
    else:
        return render(request, "login.html")


# @require_POST
def logout_view(request):
    logout(request)
    return redirect("login")
