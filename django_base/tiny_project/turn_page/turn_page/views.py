from django.http import HttpResponse
from django.shortcuts import render


def index_view(request):
    return render(request, "base.html")

def page_view(request,n):
    return render(request,"page%s.html"%n)


