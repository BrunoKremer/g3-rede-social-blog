from django.shortcuts import render
from django.http import HttpResponse, request, response
from django.views import generic
from .models import Publicacao
from django.urls.base import reverse_lazy
from .forms import Publicacao_form 

def feed(request):
    posts = Publicacao.objects.all()
    if request.method == 'POST':
       form = Publicacao_form(request.POST)
       if form.is_valid():
           data = Publicacao_form()
           data.usuario = form.cleaned_data['usuario']
           data.conteudo = form.cleaned_data['conteudo']
           data.foto = form.cleaned_data['foto']
           
           data.save()
    else:
        form = Publicacao_form()
    context = {"posts":posts, "form":form}
    return render (request, "social/feed.html", context)
