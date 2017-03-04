# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'created', max_length=120, choices=[(b'created', b'Created'), (b'paid', b'Paid'), (b'shipped', b'Shipped'), (b'refunded', b'Refunded')])),
                ('shipping_total_price', models.DecimalField(default=5.99, max_digits=50, decimal_places=2)),
                ('order_total', models.DecimalField(max_digits=50, decimal_places=2)),
                ('order_id', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=120, choices=[(b'billing', b'Billing'), (b'shipping', b'Shipping')])),
                ('street', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120, choices=[(b'A', b'ENSANCHES A '), (b'B', b'ENSANCHES B '), (b'C', b'ENSANCHES C '), (b'D', b'ENSANCHES D ')])),
                ('state', models.CharField(max_length=120)),
                ('zipcode', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='UserCheckout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('braintree_id', models.CharField(max_length=120, null=True, blank=True)),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='useraddress',
            name='user',
            field=models.ForeignKey(to='orders.UserCheckout'),
        ),
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(related_name='billing_address', to='orders.UserAddress', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(to='carts.Cart'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(related_name='shipping_address', to='orders.UserAddress', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(to='orders.UserCheckout', null=True),
        ),
    ]
