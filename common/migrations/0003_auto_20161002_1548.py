# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-02 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
        ('common', '0002_user_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='team',
        ),
        migrations.AddField(
            model_name='user',
            name='teams',
            field=models.ManyToManyField(blank=True, null=True, to='team.Team'),
        ),
    ]
