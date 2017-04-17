# -*- coding: utf-8 -*-
from __future__ import unicode_literals


"""
Created on 14.04.17.
(c) Ivan Semernyakov <direct@beatum-group.ru>
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from project.apps.interpoint.models import ToDoList


def make_task():
    """Создаём список задачь"""
    try:
        all_users = User.objects.filter(is_active=True)
        for item in all_users:
            count = 0
            while count <= 4:
                count += 1
                task_title = "Task title %d" % count
                ToDoList.objects.create(user=item, task_title=task_title)
                print("Create task %d for %s" % (count, item.username))
    except Exception as e:
        print (e)
        raise


class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        make_task()


