from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from .models import Post, Comment


# def post_list(request):
#     return render(request, 'blog/post_list.html')

post_list = ListView.as_view(model=Post)
