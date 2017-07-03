# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soft_lib', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='booked_to',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='soft_lib.User'),
            preserve_default=False,
        ),
    ]
