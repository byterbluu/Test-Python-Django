from django.shortcuts import render, HttpResponse

from .models import Post

# Create your views here.

def posts(request):
    first_post = Post.objects.first()
    posts = Post.objects.all()
    return render(request, 'blogs.html', {'posts': posts, 'first_post': first_post})

def post(request, id):
    blog = Post.objects.get(id=id)
    return render(request, 'blog.html', {'blog': blog})