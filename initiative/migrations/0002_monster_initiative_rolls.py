# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-17 21:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initiative', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='initiative_rolls',
            field=models.CharField(default=0, max_length=50, validators=[django.core.validators.int_list_validator]),
        ),
    ]
