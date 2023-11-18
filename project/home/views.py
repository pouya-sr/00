from django.shortcuts import render
from django.http import httpResponse 
# Create your views here.
def x(request):
    return httpResponse('hello user ...')