# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0042_order_expires'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalSetting',
            fields=[
                ('key', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('value', models.TextField()),
            ],
        ),
    ]
