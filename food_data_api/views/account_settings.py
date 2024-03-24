from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages


def settings_page(request):
    # Get the logged-in user's name or username
    user = request.user
    user_name = request.user.get_full_name() or request.user.username

    user_group = (
        request.user.groups.first().name if request.user.groups.exists() else "No Group"
    )

    context = {"user_name": user_name, "user_group": user_group, "user": user}
    return render(request, "profile.html", context)


@login_required
def update_profile(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get("first_name", user.first_name)
        user.last_name = request.POST.get("last_name", user.last_name)
        user.email = request.POST.get("email", user.email)
        user.username = request.POST.get("username", user.username)
        print(user.username)

        try:
            user.save()
            messages.success(request, "Your profile was successfully updated!")
        except Exception as e:
            messages.error(request, "There was an error updating your profile.")

        return redirect("settings")

    else:
        return render(request, "profile.html")
