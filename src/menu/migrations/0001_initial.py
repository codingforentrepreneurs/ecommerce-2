# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuDish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=False)),
                ('day', models.CharField(max_length=50, choices=[(b'0', b'Lunes'), (b'1', b'Martes'), (b'2', b'Miercoles'), (b'3', b'Jueves'), (b'4', b'Viernes'), (b'5', b'Sabado'), (b'6', b'Libre')])),
                ('dish1', models.ForeignKey(related_name='dish1', to='products.Product')),
                ('dish2', models.ForeignKey(related_name='dish2', to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='MenuWeek',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('week', models.CharField(max_length=120, null=True, blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='menudish',
            name='menu_week',
            field=models.ForeignKey(to='menu.MenuWeek'),
        ),
    ]
