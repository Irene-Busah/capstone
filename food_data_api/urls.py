from django.urls import path
from .views.expired_products import (
    products_nearing_expiry,
    dashboard_page,
    expired_products_by_category_api,
    coming_soon,
)
from .views.sales import sales_by_category_api
from .views.consumption import frequently_consumed_by_region_api
from .views.account_settings import settings_page, update_profile
from .views.notifications import notification_page
from .views.security_settings import (
    security_settings_page,
    delete_account,
    change_password,
)
from .views.notification_settings import notification_settings_page
from .views.authentication import signup_api, login_api, logout_view
from .views.notifications import notifications_api
from .views.inventory_rate import inventory_and_purchase_rate_api
from .views.analysis import insights_and_suggestions_api


urlpatterns = [
    # coming-soon page
    path("coming-soon/", coming_soon, name="coming_soon_page"),
    # authentication
    path("signup/", signup_api, name="signup-api"),
    path("logout/", logout_view, name="logout"),
    # pages urls
    path("dashboard/", dashboard_page, name="index"),
    path("settings/", settings_page, name="settings"),
    path("notifications/", notification_page, name="notifications"),
    path(
        "notifications/settings/",
        notification_settings_page,
        name="notification-settings",
    ),
    path("settings/security/", security_settings_page, name="security-settings"),
    # apis url
    path("expiry-products/", products_nearing_expiry, name="products-nearing-expiry"),
    path(
        "expired-products-by-category/",
        expired_products_by_category_api,
        name="expired_products_by_category_api",
    ),
    path("sales-by-category/", sales_by_category_api, name="sales_by_category_api"),
    path(
        "frequently-consumed-by-region/",
        frequently_consumed_by_region_api,
        name="frequently_consumed_by_region_api",
    ),
    path("update-profile/", update_profile, name="update_profile"),
    path("delete-account/", delete_account, name="delete_account"),
    path("change-password/", change_password, name="change_password"),
    path("notification-messages/", notifications_api, name="notification-messages"),
    path(
        "inventory-purchase-rate/",
        inventory_and_purchase_rate_api,
        name="inventory-purchase-rate-api",
    ),
    path("analysis/", insights_and_suggestions_api, name="analysis"),
]
