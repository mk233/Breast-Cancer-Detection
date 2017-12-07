# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def content_file_name(instance, filename):
    ext=filename.split('.')[-1]
    filename="%s.%s" % ("regressionDataSet" , ext)

    return "user_{id}/{file}".format(id=instance, file=filename)

class filename(models.Model):
    file=models.FileField(upload_to=content_file_name)
    Training=models.CharField(max_length=250)
    Testing=models.CharField(max_length=250)
    email_id=models.EmailField()
    id1= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)



    def __unicode__(self):
        return str(self.id1)

