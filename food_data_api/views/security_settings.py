from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login


def security_settings_page(request):
    user = request.user
    user_name = request.user.get_full_name() or request.user.username

    user_group = (
        request.user.groups.first().name if request.user.groups.exists() else "No Group"
    )

    context = {"user_name": user_name, "user_group": user_group, "user": user}
    return render(request, "security-settings.html", context)


@login_required
@require_POST
def delete_account(request):
    user = request.user
    user.delete()
    messages.success(request, "Your account has been successfully deleted.")
    return redirect("signup-api")


@login_required
@require_POST
def change_password(request):
    if request.method == "POST":
        user = request.user
        new_password = request.POST.get("new_password")
        confirm_new_password = request.POST.get("confirm_new_password")

        if new_password == confirm_new_password:
            user.set_password(new_password)
            user.save()

            # Re-authenticate user
            reauth_user = authenticate(username=user.username, password=new_password)
            if reauth_user:
                login(request, reauth_user)
                messages.success(
                    request, "Your password has been successfully changed."
                )
            else:
                messages.error(
                    request,
                    "There was an error re-authenticating. Please log in again.",
                )
        else:
            messages.error(request, "Passwords do not match.")

    return redirect("security-settings")
