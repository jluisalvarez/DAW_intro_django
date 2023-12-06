from django.shortcuts import render, redirect

from blog.models import Post
from blog.forms import PostForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = PostForm()
    return render(request, 'posts/form.html', {'form': form})


def details(request, id):
    try:
        post = Post.objects.get(pk=id)
    except Post.DoesNotExist:
        msg = "Post #" + str(id) + " no encontrado"
        return render(request, 'index.html', {'msg': msg})
    msg = "Detalles Post: " + str(id)
    return render(request, 'details.html', {'msg': msg, 'post': post})


def edit(request, id):
    try:
        post = Post.objects.get(pk=id)
    except Post.DoesNotExist:
        msg = "Post #" + str(id) + " no encontrado"
        return render(request, 'index.html', {'msg': msg})  

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = PostForm(instance=post)
 
    return render(request, 'posts/form.html', {'form': form, 'id':id})


def delete(request, id):
    try:
        post = Post.objects.get(pk=id)
        post.delete()
    except Post.DoesNotExist:
        msg = "Post #" + str(id) + " no encontrado"
        return render(request, 'index.html', {'msg': msg})
    msg = "Borrado Post: " + str(id)
    posts = Post.objects.all()
    return render(request, 'index.html', {'msg': msg, 'posts': posts})

def like(request, id):
    try:
        post = Post.objects.get(pk=id)
        post.likes = post.likes+1
        post.save()
    except Post.DoesNotExist:
        msg = "Post #" + str(id) + " no encontrado"
        return render(request, 'index.html', {'msg': msg})    
    msg = "Like Post: " + str(id)
    return render(request, 'details.html', {'msg': msg, 'post': post})
