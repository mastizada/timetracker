# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-02 15:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
        ('project', '0004_auto_20161001_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='team.Team'),
            preserve_default=False,
        ),
    ]
