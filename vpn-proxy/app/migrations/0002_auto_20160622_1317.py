# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-22 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forwarding',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='forwarding',
            name='dst_addr',
            field=models.GenericIPAddressField(protocol='IPv4'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
