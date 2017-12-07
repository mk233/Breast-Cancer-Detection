# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import file.models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filename',
            name='job_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='filename',
            name='file',
            field=models.FileField(upload_to=file.models.content_file_name),
        ),
    ]