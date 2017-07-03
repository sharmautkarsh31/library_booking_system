# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 11:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soft_lib', '0003_auto_20170630_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='issued_book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_issued_book', to='soft_lib.Book'),
        ),
        migrations.AlterField(
            model_name='user',
            name='past_books',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_past_books', to='soft_lib.Book'),
        ),
    ]
