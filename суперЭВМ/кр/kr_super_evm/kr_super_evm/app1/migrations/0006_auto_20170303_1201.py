# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 09:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0005_auto_20170303_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additive',
            name='user_id',
        ),
        migrations.AddField(
            model_name='additive',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
