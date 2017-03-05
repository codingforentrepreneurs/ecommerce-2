# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20170304_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuweek',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='menuweek',
            name='start_date',
            field=models.DateField(),
        ),
    ]
