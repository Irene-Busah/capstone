from django.shortcuts import render


def notification_settings_page(request):
    user = request.user
    user_name = request.user.get_full_name() or request.user.username

    user_group = (
        request.user.groups.first().name if request.user.groups.exists() else "No Group"
    )

    context = {"user_name": user_name, "user_group": user_group, "user": user}
    return render(request, "notification-settings.html", context)
