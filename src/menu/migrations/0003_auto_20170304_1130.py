# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20170303_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menudish',
            name='day',
            field=models.CharField(max_length=50, choices=[(b'Lunes', b'Lunes'), (b'Martes', b'Martes'), (b'Miercoles', b'Miercoles'), (b'Jueves', b'Jueves'), (b'Viernes', b'Viernes'), (b'Sabado', b'Sabado'), (b'Libre', b'Libre')]),
        ),
        migrations.AlterField(
            model_name='menudish',
            name='menu_week',
            field=models.ForeignKey(related_name='menu_week', blank=True, to='menu.MenuWeek', null=True),
        ),
    ]
