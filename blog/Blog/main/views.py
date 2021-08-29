from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.http import HttpResponse, request


# from django.contrib.auth.models import User
from .models import Post, Categoria, Comentarios
from django.core.paginator import Paginator



def home(request):
    post =  get_list_or_404(Post)
    paginator = Paginator(post, 2) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categoria =  get_list_or_404(Categoria)
    

    context = {'post':post, 'categoria':categoria, 'page_obj': page_obj}
    return render(request, 'blog/home.html', context)
        
    

# Create your views here.
