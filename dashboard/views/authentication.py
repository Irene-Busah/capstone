from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.urls import reverse
from core.emails.accounts.emails import send_welcome_email


@require_POST
def signup_view(request):
    if request.method == "POST":
        User = get_user_model()
        username = request.POST.get("username")
        email = request.POST.get("email")
        full_name = request.POST.get("fullName")
        account_type = request.POST.get("account_type")
        password = request.POST.get("password")

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists"}, status=400)

        # Create the user
        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        user.first_name, user.last_name = (full_name.split(" ", 1) + [""])[:2]
        user.save()

        # Assign to group based on account type
        group, _ = Group.objects.get_or_create(name=account_type)
        user.groups.add(group)

        # Send the welcome email
        login_link = "http://127.0.0.1:8000"
        send_welcome_email(
            recipient_email=email,
            first_name=user.first_name,
            password=password,
            login_link=login_link,
        )

        login(request, user)

        # Return the successful response
        return JsonResponse({"message": "User created successfully"}, status=201)

    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
