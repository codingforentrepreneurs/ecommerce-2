# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menudish',
            name='dish1',
            field=models.ForeignKey(related_name='dish1', default=b'Default', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='menudish',
            name='dish2',
            field=models.ForeignKey(related_name='dish2', default=b'Default', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='menudish',
            name='menu_week',
            field=models.ForeignKey(blank=True, to='menu.MenuWeek', null=True),
        ),
    ]
