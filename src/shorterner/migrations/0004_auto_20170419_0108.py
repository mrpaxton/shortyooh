# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-19 01:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shorterner', '0003_auto_20170419_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shorturl',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
