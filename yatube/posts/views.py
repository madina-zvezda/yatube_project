from turtle import title
from django.shortcuts import render, get_object_or_404
from .models import Post, Group

# Create your views here.

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Это главная страница проекта Yatube'
    templates = 'posts/index.html'
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, templates, context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    title = f'Зписи сообщества {group.title}'
    templates = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, templates, context) 

