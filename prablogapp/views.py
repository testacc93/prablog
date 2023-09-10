from django.shortcuts import render
from .models import Blog

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})


def blogbyurl(request, blog_name):
    blog = Blog.objects.get(title=blog_name)
    print(blog.__dict__)
    return render(request, 'blog.html', {'blog':blog})
