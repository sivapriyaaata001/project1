from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def siva(request):
    return HttpResponse('i have created a view')
