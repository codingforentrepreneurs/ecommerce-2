# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20150903_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='city',
            field=models.CharField(max_length=120, choices=[(b'A', b'ENSANCHES A '), (b'B', b'ENSANCHES B '), (b'C', b'ENSANCHES C '), (b'D', b'ENSANCHES D ')]),
        ),
    ]
