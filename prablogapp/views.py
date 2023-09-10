from django.shortcuts import render
from .models import Blog

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})


def blogbyurl(request, blog_name):
    blog = Blog.objects.get(title=blog_name)
    return render(request, 'blog.html', {'blog':blog})
