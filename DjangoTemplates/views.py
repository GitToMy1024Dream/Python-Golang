# -*- coding:utf-8 -*-

# 使用httpresponse

from django.http import HttpResponse

def Hello(request):
    return HttpResponse("Hello, this is my first django web.")

# 使用render

import datetime
from django.template import Template, Context
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.loader import get_template

def Hello(request):
    context = {}
    context['hello'] = 'Hello world, i am Tony!'
    return render(request, 'hello.html', context)

def current_datetime(request):
    now_time = datetime.datetime.now()
    html = "<html><body><p>It is time：%s .</p></body></html>" % now_time
    return HttpResponse(html)


# 使用模板
def current_datetime(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It time is {{time}}</body></html>")
    html = t.render(Context({'time':now}))
    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    context = {'current_date': now}
    return render_to_response('current_datetime.html', context)

def hours_datetime(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        print 'offset key error'
    time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body><p>It is time：%s (%s).</p></body></html>" % (time, offset)
    return HttpResponse(html)