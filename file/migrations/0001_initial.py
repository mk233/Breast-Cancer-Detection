# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='filename',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=b'')),
                ('Training', models.CharField(max_length=250)),
                ('Testing', models.CharField(max_length=250)),
                ('email_id', models.EmailField(max_length=254)),
            ],
        ),
    ]
