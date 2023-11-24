from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def index(request):
    data = {"header":"index"}
    return render(request, "guitarlesson\index.html", context=data)

def about(request):
    data = {"header":"about"}
    return render(request, "guitarlesson\index.html", context=data)

def lessons(request):
    data = {"header":"lessons"}
    return render(request, "guitarlesson\index.html", context=data)

def contacts(request):
    data = {"header":"contacts"}
    return render(request, "guitarlesson\index.html", context=data)