from django.contrib import admin

from .models import MenuWeek, MenuDish

class MenuInlines(admin.TabularInline):
    model = MenuDish
    extra = 0
    max_num = 6


class MenuAdmin(admin.ModelAdmin):
   list_display = ['__unicode__', 'start_date', 'end_date', 'active']
   ordering = ['start_date']
   inlines = [MenuInlines]

   class Meta:
       model = MenuWeek

class MenuDishAdmin(admin.ModelAdmin):
    list_display = ['menu_week','dish1', 'dish2', 'day']

    class Meta:
        model = MenuDish

# Register your models here.


admin.site.register(MenuWeek, MenuAdmin)

admin.site.register(MenuDish, MenuDishAdmin)
