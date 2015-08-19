from django.contrib import admin

# Register your models here.


from .models import Product, Variation

admin.site.register(Product)

admin.site.register(Variation)