from django.apps import AppConfig


class FoodDataApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "food_data_api"

    def ready(self):
        import food_data_api.models.signals
