# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Created on 11.04.17.
(c) Ivan Semernyakov <direct@beatum-group.ru>
"""

from django.shortcuts import render


def home(request):
    return render(request, "home.html")
