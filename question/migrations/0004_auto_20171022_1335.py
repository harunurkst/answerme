# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 13:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20171022_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='subscribers',
            field=models.ManyToManyField(blank=True, null=True, related_name='subscribed', to=settings.AUTH_USER_MODEL),
        ),
    ]
