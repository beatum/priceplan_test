# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Created on 17.04.17.
(c) Ivan Semernyakov <direct@beatum-group.ru>
"""

from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Article, ToDoList


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_title', 'user', 'task_is_completed',
                    'task_in_history', 'task_time')
    list_display_links = ('task_title',)
    list_filter = ('user', 'task_is_completed', 'task_in_history',)
    date_hierarchy = ('task_time')


admin.site.unregister(Group)
