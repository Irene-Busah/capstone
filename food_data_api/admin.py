from django.contrib import admin

from .models.category import Category
from .models.product import Product
from .models.people import Supplier
from .models.region_store import Region, Store
from .models.sales import Sale, Transaction, InventoryAdjustment


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Supplier)
# admin.site.register(Customer)
admin.site.register(Region)
admin.site.register(Store)
admin.site.register(Sale)
admin.site.register(Transaction)
admin.site.register(InventoryAdjustment)
