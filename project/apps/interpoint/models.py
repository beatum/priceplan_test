# -*- coding: utf-8 -*-
from __future__ import unicode_literals


"""
Created on 11.04.17.
(c) Ivan Semernyakov <direct@beatum-group.ru>
"""

from django.db import models
from django.conf import settings


class ToDoList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    task_title = models.CharField(max_length=254)
    task_is_completed = models.BooleanField(default=False)
    task_in_history = models.BooleanField(default=False)
    task_time = models.DateTimeField(auto_now=True, editable=False, blank=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.task_title

    def __unicode__(self):
        return '%s' % self.task_title


class Article(models.Model):
    field1 = models.CharField(max_length=254)
    field2 = models.CharField(max_length=254)
    field3 = models.CharField(max_length=254)
    field4 = models.CharField(max_length=254)
    field5 = models.IntegerField()
    
    def __str__(self):
        return self.field1

    def __unicode__(self):
        return '%s' % self.field1
