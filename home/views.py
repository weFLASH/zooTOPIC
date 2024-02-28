from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render (request,'home.html')
# Create your views here.

def introduce(request):
    return render(request, 'introduction.html')