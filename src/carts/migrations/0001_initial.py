# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('subtotal', models.DecimalField(default=25.0, max_digits=50, decimal_places=2)),
                ('tax_percentage', models.DecimalField(default=0.085, max_digits=10, decimal_places=5)),
                ('tax_total', models.DecimalField(default=25.0, max_digits=50, decimal_places=2)),
                ('total', models.DecimalField(default=25.0, max_digits=50, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('line_item_total', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cart', models.ForeignKey(to='carts.Cart')),
                ('item', models.ForeignKey(to='products.Variation')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(to='products.Variation', through='carts.CartItem'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
