"""
URL configuration for ppal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.http import HttpResponse

def holamundo2(request):
 return HttpResponse("<h1>Hola Mundo!</h1>")

from django.shortcuts import render

from blog.views import index, new_post

def holamundo(request):
    return render(request, 'index.html', {})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hm/', holamundo),

    path('', index, name='index'),
    path('new', new_post, name='new')
]
