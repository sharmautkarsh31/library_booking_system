# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 10:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soft_lib', '0002_book_booked_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='issued',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='issued_book',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_issued_book', to='soft_lib.Book'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='past_books',
            field=models.ManyToManyField(related_name='user_past_books', to='soft_lib.Book'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
