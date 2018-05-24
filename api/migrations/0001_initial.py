# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-18 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('name', models.CharField(max_length=200,default="none",null=True)),
                ('photoRef', models.CharField(max_length=500,default="none")),
                ('placeId',models.CharField(max_length=200,primary_key=True,default="none")),
                ('vicinty',models.CharField(max_length=500,default="none")),
                ('latitude',models.FloatField(default=0)),
                ('longitude',models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('is_guide', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(default='None', max_length=200)),
                ('tripName', models.CharField(max_length=200, default="None")),
                ('tripDescription', models.CharField(max_length=500, default="None")),
                ('guides', models.ManyToManyField(to='api.User')),
                ('places', models.ManyToManyField(to='api.Place')),
            ],
        ),
    ]
