from django.shortcuts import render, redirect

from blog.models import Post
from blog.forms import PostForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'msg': 'Todo Ok!', 'posts': posts})

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = PostForm()
    return render(request, 'posts/form.html', {'form': form})
