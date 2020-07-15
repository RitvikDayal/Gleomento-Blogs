from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Home Route
def home(request):
     return render(request, 'blog/index.html', {'title': 'Home'})

# Blog Route
def blog(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Blog'
    }

    return render(request, 'blog/blog.html', context=context)

# About Route
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})