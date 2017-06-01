# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
    print(User.objects.all())
    return render(request, 'ratingauth/index.html')
