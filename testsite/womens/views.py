from django.http import HttpResponse
from django.shortcuts import render

from .models import Women

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]

def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        }

    return render(request, 'womens/index.html', context=context)

def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте',
        }

    return render(request, 'womens/about.html', context=context)

def show_post(requests, post_id):
    return HttpResponse(f'Пост = {post_id}')

def addpage(requests):
    return HttpResponse('Добавить статью')

def contact(requests):
    return HttpResponse('Контакты')

def login(requests):
    return HttpResponse('Авторизация')
