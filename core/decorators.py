from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from functools import wraps
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


def group_required(view_func):
    @wraps(view_func)
    def _wrapped_view_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")

        user_groups = request.user.groups.values_list("name", flat=True)
        if "Retailer" in user_groups:
            # If user is a Retailer, call the original view
            return view_func(request, *args, **kwargs)
        elif "Manufacturer" in user_groups or "Wholesaler" in user_groups:
            # If user is a Manufacturer or Wholesaler, redirect to the coming soon page
            return redirect("coming_soon_page")
        else:
            # If user doesn't belong to any expected group, raise a permission denied error
            raise PermissionDenied

    return _wrapped_view_func
