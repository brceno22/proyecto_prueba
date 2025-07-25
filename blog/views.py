from django.shortcuts import render
from .models import Post
# Create your views here.
def lista_posts(request):
    posts = Post.objects.all() # obtener todos los posts
    return render(request, 'blog/lista_posts.html', {'posts': posts})

