# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    username = models.CharField(max_length=200, blank=True, null=True)
    remote_link = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.username


class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Entry(models.Model):
    title = models.CharField(max_length=300, blank=True, null=False)
    content = models.TextField()
    extra_id = models.CharField(max_length=500, unique=True)
    published = models.DateTimeField(blank=True, null=True)
    authors = models.ManyToManyField(Author)
    tags = models.ManyToManyField(Tag)
    predefined_field = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.extra_id
