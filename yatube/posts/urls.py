from django.urls import path
from . import views
from django.contrib import admin

app_name = 'posts'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('group/<slug:slug>/', views.group_posts, name='posts_list'),
    path('admin/', admin.site.urls)
] 
