from django.contrib import admin
from .models import Product, ProductCategory, Contacts


admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Contacts)
