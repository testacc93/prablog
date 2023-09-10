from django.shortcuts import render
from .models import Blog

def home(request):
    blogs = Blog.objects.all()
    print(dir(blogs[0].image_url.image_url.url))
    return render(request, 'home.html', {'blogs':blogs})


def blogbyurl(request, blog_name):
    blog = Blog.objects.get(title=blog_name)
    return render(request, 'blog.html', {'blog':blog})
