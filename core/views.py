from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(resquest):

    return HttpResponse('<h1>Hello Word</h1>')