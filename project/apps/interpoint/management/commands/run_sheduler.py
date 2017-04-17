# -*- coding: utf-8 -*-
from __future__ import unicode_literals


"""
Created on 17.04.17.
(c) Ivan Semernyakov <direct@beatum-group.ru>
"""

from datetime import timedelta
from django.utils import timezone
from django.core.management.base import BaseCommand
from project.apps.interpoint.management.commands.make_task import make_task
from project.apps.interpoint.management.commands.clear_task import clear_task
import django_rq


star_date_and_time = timezone.now()
# время первого старта в формате datetime(2020, 1, 1, 3, 4)

end_date_and_time = timezone.now() + timedelta(hours=8)
# смещение во времени, предположим, что рабочий день
# длиться 8 часов

interval = 60*60*24
# интервал повторений, в секундах, скажем каждые 24 часа

repeat = 31
# кол-во повторений


class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        self.make()
    
    def make(self):

        scheduler = django_rq.get_scheduler('default')

        print 'Make task every day at %s' % star_date_and_time

        scheduler.schedule(
            scheduled_time=timezone.now(),  # установим время начала задачи
            func=make_task,   # вызываемая функция
            args=[],
            interval=interval,  # интервал в секундах, каждые 24 часа
            repeat=repeat,   # количество повторений
        )

        print 'Clean task every day at %s' % end_date_and_time

        scheduler.schedule(
            scheduled_time=end_date_and_time,
            func=clear_task,
            args=[],
            interval=interval,
            repeat=repeat,
        )
