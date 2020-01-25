# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-08-14 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=1)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
    ]
