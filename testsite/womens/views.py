from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('главная страница')

def categories(request):
    return HttpResponse('категории')
