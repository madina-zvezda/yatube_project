from re import template
from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    templates = 'posts/index.html'
    title = 'Социльная сеть для блогеров'

    posts = Post.objects.all()

    context = {
        'title': title,
        'text': 'Это главная страница проекта Yatube',
        'posts': posts,
    }
    return render(request, templates, context) 

def group_posts(request, slug):
    templates = 'posts/group_list.html'
    title = 'Группы проекта Yatube'
    context = {
        'title': title,
        'text': 'Здесь будет информация о группах проекта Yatube',
    }
    return render(request, templates, context)

