# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_nbs', '0002_account_limited_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_limited',
            name='account',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
