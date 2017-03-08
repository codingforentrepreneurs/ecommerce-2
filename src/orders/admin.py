from django.contrib import admin

# Register your models here.


from .models import UserCheckout, UserAddress, Order

class AdminUserCheckout(admin.ModelAdmin):
    list_display = ['pk','__unicode__']

    class Meta:
        model = UserCheckout
        ordering = ['pk']


admin.site.register(UserCheckout,AdminUserCheckout)


admin.site.register(UserAddress)

class AdminOrders(admin.ModelAdmin):
    list_display = ['id','user']

admin.site.register(Order, AdminOrders)