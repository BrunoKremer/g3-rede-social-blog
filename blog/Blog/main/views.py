from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.http import HttpResponse, request


# from django.contrib.auth.models import User
from .models import Post, Categoria
# from rest_framework.renderers import TemplateHTMLRenderer
# from rest_framework.response import Response
# from rest_framework.views import APIView


def home(request):
    post =  get_list_or_404(Post)
    return render(request, 'blog/home.html', {'post':post})

def filter_categoria(request):
    categoria =  get_list_or_404(Categoria)
    return render(request, "blog/home.html", {'categoria':categoria})
    
    

# Create your views here.
