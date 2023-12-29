from django.shortcuts import render

from app.models import *

from django.http import HttpResponse
# Create your views here.

def form(request):

    if request.method == 'POST':
        tn = request.POST['tn']
        TO = Topic.objects.get_or_create(topic_name = tn)[0]
        TO.save()
        QLTO = Topic.objects.all()
        d = {'topics':QLTO}
        return render(request,'display_topic.html',d)

    return render(request,'form.html')

def display_topic(request):
    QLTO = Topic.objects.all()
    d = {'topics':QLTO}
    return render(request,'display_topic.html',d)

def insert_webpage(request):
    QLTO = Topic.objects.all()
    d = {'topics':QLTO}

    if request.method == 'POST':
        tn = request.POST['tn']
        n = request.POST['n']
        u = request.POST['u']
        e = request.POST['e']
        TO = Topic.objects.get(topic_name = tn)
        WO = Webpage.objects.get_or_create(topic_name = TO,name = n,url = u,email = e)[0]
        WO.save()

        QLWO = Webpage.objects.all()
        d = {'webpages':QLWO}
        return render(request,'display_webpage.html',d)

    return render(request,'insert_webpage.html',d)


def display_webpage(request):
    QLWO = Webpage.objects.all()
    d = {'webpages':QLWO}
    return render(request,'display_webpage.html',d)