# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .forms import filenameForm
from .models import filename

class filenameAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","Training","Testing"]
    form=filenameForm
   # class Meta:
   #     model = filename

admin.site.register(filename, filenameAdmin)