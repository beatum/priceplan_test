# -*- coding: utf-8 -*-
from __future__ import unicode_literals


"""
Created on 14.04.17.
(c) Ivan Semernyakov <direct@beatum-group.ru>
"""

from django.core.management.base import BaseCommand
from project.apps.interpoint.models import ToDoList


def clear_task():
    """ Отправляем все задачи в историю """
    try:
        task_list = ToDoList.objects.all()
        for item in task_list:
            item.task_in_history = True
            item.save()
        print('All tasks (%d) pushed to history' % len(task_list))
    except Exception as (e):
        print('Tasks not found')
        raise


class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        clear_task()


