from django.http import HttpResponse
from django.shortcuts import render

from .models import Women

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    posts = Women.objects.all()

    return render(
        request,
        'womens/index.html',
        {'posts': posts,
            'menu': menu,
            'title': 'Главная страница'})

def about(request):
    return render(
        request,
        'women/about.html',
        {'menu': menu, 'title': 'О сайте'})
