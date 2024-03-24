from django.urls import path
from food_data_api.views.authentication import login_api, signUp_page

urlpatterns = [
    path("", login_api, name="login"),
    path("sign-up/", signUp_page, name="sign-up"),
]
