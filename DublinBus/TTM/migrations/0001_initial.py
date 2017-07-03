# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('RouteID', models.CharField(max_length=5, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Stops',
            fields=[
                ('StopID', models.IntegerField(primary_key=True, serialize=False)),
                ('BusLine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TTM.Routes')),
            ],
        ),
    ]
