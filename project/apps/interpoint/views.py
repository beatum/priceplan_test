# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Created on 12.04.17.
(c) Ivan Semernyakov <direct@beatum-group.ru>
"""

from django.contrib.auth.models import User
from django.forms import ModelForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoList


class ToDoForm(ModelForm):
    class Meta:
        model = ToDoList
        fields = ['task_is_completed']


def all_task(request):
    task_list, task_item = None, None
    
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/admin/')
    else:
        user = request.user
    
    try:
        task_item = ToDoList.objects.filter(task_is_completed=False,
                                            task_in_history=False,
                                            user=user).earliest(field_name='id')
        
        task_list = ToDoList.objects.filter(task_is_completed=False,
                                            task_in_history=False,
                                            user=user).exclude(
                                            id=task_item.id) \
            .order_by('id')
    except ToDoList.DoesNotExist as e:
        print (e)
    
    if request.method == 'POST':
        task_form = ToDoForm(request.POST, instance=task_item)
        if task_form.is_valid():
            task_form.save()
            return HttpResponseRedirect('/todo/')
    else:
        task_form = ToDoForm()
    
    return render(request, 'todo.html', {
        'task_form': task_form,
        'task_list': task_list,
        'task_item': task_item
        })


def orm(request):
    from django.utils import timezone
    from datetime import timedelta
    
    get_all_task, task_for_day, count_task_for_day, get_user, \
    get_user_task_completed, get_user_task_uncompleted = None, None, \
        None, None, None, None

    try:
        get_all_task = ToDoList.objects.all()
    except ToDoList.DoesNotExist as e:
        print (e)

    if get_all_task:
        # список выполненных задач за определенный день (а точнее за последние
        # 24 часа)
        task_for_day = ToDoList.objects.filter(
            task_is_completed=True,
            task_time__lte=timezone.now(),
            task_time__gte=timezone.now() - timedelta(days=1)
        )  # либо можно сделать так .filter(task_time__day=1)
        
        if task_for_day:
            # число всех выполненных задач за определенный день
            count_task_for_day = len(task_for_day)
    
    try:
        get_user = User.objects.latest(field_name='id')
    except User.DoesNotExist as (e):
        print (e)

    if get_user:
        get_user_task_completed = get_user.todolist_set.filter(
            task_is_completed=True)
        # список выполненных задач определенного сотрудника (имя задачи, время,
        # имя сотрудника)
        
        get_user_task_uncompleted = get_user.todolist_set.exclude(
            task_is_completed=True).filter(task_time__lte=timezone.now(),
            task_time__gte=timezone.now() - timedelta(days=1)
        )
        # список невыполненных задач определенного сотрудника за любой день
    
    return render(request, 'orm.html', {
        'task_for_day': task_for_day,
        'count_task_for_day': count_task_for_day,
        'get_user_task_completed': get_user_task_completed,
        'get_user_task_uncompleted': get_user_task_uncompleted
    })
