# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from collections import OrderedDict
from datetime import datetime
import uuid, json, math


def index(request):
    return render(request, "shibei_web/index.html")


def gallery(request):
    return render(request, "shibei_web/gallery.html")


def codes(request):
    return render(request, "shibei_web/codes.html")


def code(request):
    return render(request, "shibei_web/code.html")


def contact(request):
    return render(request, "shibei_web/contact.html")


def about(request):
    return render(request, "shibei_web/about.html")


def services1(request):
    return render(request, "shibei_web/services1.html")


def services2(request):
    return render(request, "shibei_web/services2.html")


def services3(request):
    return render(request, "shibei_web/services3.html")


def services4(request):
    return render(request, "shibei_web/services4.html")


def services5(request):
    return render(request, "shibei_web/services5.html")
#
#
def services6(request):
    return render(request, "shibei_web/services6.html")