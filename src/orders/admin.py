from django.contrib import admin

# Register your models here.


from .models import UserCheckout, UserAddress


admin.site.register(UserCheckout)


admin.site.register(UserAddress)