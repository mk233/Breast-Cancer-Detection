# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0005_remove_filename_job_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filename',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
