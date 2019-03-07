# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-06 16:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='description',
        ),
        migrations.AddField(
            model_name='image',
            name='image_description',
            field=models.TextField(default=django.utils.timezone.now, max_length=400),
            preserve_default=False,
        ),
    ]
