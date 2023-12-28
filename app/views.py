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

'''def insert_webpage(request):
    QLWO = Webpage.objects.all()
    d = {'webpages':QLWO}
    return render(request,'insert_webpage.html',d)'''