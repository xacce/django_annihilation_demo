# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from test_app import models

admin.site.register(models.Entry)
admin.site.register(models.Tag)
admin.site.register(models.Author)
