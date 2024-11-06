from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
def detail_view(request:HttpRequest):
    return render(request,"plant/detail.html")