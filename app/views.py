from django.shortcuts import render

# Create your views here.
from app.forms import *

def topicform(request):
    form=TopicForm()
    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            form_data.save()

    return render(request,'topicform.html',context={'form':form})


def webpageform(request):
    form=WebpageForm()
    if request.method=="POST":
        form_data=WebpageForm(request.POST)
        if form_data.is_valid():
            form_data.save()
    return render(request,'webpageform.html',context={'form':form})

def accessform(request):
    form=AccessForm()
    if request.method=="POST":
        form_data=AccessForm(request.POST)
        if form_data.is_valid():
            form_data.save()
    
    return render(request,'accessform.html',context={'form':form})












