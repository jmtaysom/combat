# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initiative', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='notes',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]