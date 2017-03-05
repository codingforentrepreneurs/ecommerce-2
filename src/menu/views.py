from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic.list import ListView
from django import template
from datetime import date, datetime, timedelta

from .models import MenuWeek, MenuDish

register = template.Library()


@register.filter(expects_localtime=True)
def is_future(value):
    if isinstance(value, datetime):
        value = value.date()
    return value > date.today()


@register.filter(expects_localtime=True)
def is_past(value):
    if isinstance(value, datetime):
        value = value.date()
    return value < date.today()


class MenuListView(ListView):
    model = MenuWeek
# queryset = MenuDish.objects.all()
# filter_class = MenuDish
