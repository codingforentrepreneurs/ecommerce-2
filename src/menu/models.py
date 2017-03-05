from django.db import models
from django.db.models.signals import post_save
from products.models import Product

#Create your models here.
Day = (
    ('Lunes', 'Lunes'),
    ('Martes', 'Martes'),
    ('Miercoles', 'Miercoles'),
    ('Jueves', 'Jueves'),
    ('Viernes', 'Viernes'),
    ('Sabado', 'Sabado'),
    ('Libre', 'Libre'),

)

class MenuWeek(models.Model):
    week = models.CharField(max_length=120, null=True, blank=True )
    start_date = models.DateField(auto_now_add=False, auto_now=False)
    end_date = models.DateField(auto_now_add=False, auto_now=False)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.week

class MenuDish(models.Model):
    dish1 = models.ForeignKey(Product, related_name='dish1', default='Default')
    dish2 = models.ForeignKey(Product, related_name='dish2', default='Default')
    active = models.BooleanField(default=False)
    day = models.CharField(max_length=50, choices=Day)
    menu_week = models.ForeignKey(MenuWeek,null=True, blank=True, related_name='menu_week')

    def __unicode__(self):
        return self.day
