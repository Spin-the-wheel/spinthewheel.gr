# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-29 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_kind_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='kind',
            name='description',
            field=models.CharField(default='thank u', max_length=500),
            preserve_default=False,
        ),
    ]
