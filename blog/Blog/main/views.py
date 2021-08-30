
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.http import HttpResponse, request, response


# from django.contrib.auth.models import User
from django.db.models import Q
from .models import Post, Categoria, Comentarios
from django.core.paginator import Paginator
from django.views import generic

def home(request):
    post =  get_list_or_404(Post)
    paginator = Paginator(post, 2) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categoria =  Categoria.objects.all()
    

    context = {'post':post, 'categoria':categoria, 'page_obj': page_obj}
    
    return render(request, 'blog/home.html', context )
        

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# class CategoriaDetailView(generic.DetailView):
#     model = Categoria
#     template_name = 'blog/categoria_detail.html'


# Create your views here.
