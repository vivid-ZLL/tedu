from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def page1_view(request):
    return HttpResponse("页面一")

def page2_view(request):
    return HttpResponse("页面二")

def page3_view(request):
    return HttpResponse("页面三")