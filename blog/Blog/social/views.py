from django.shortcuts import render,redirect
from django.http import HttpResponse, request, response
from django.views import generic
from .models import Publicacao
from django.urls.base import reverse_lazy
from .forms import Publicacao_form

def feed(request):
    posts = Publicacao.objects.all()
    comentarios = Comentario.objects.all()
    if request.method == 'POST':
        form_comentario = Comentario_publi(request.POST)
        if form_comentario.is_valid():
            data = Comentario()
            data.comentario = form_comentario.cleaned_data['comentario']
            data.foto = form_comentario.cleaned_data['foto']
            data.usuario_id = request.user.id
            data.publicacao_id = 4
            data.save()
    else:
        form_comentario = Comentario_publi()
    if request.method == 'POST':
       form = Publicacao_form(request.POST)
       if form.is_valid():
           data = Publicacao()
           data.conteudo = form.cleaned_data['conteudo']
           data.foto = form.cleaned_data['foto']
           data.usuario_id = request.user.id
           data.save()
    else:
        form = Publicacao_form()
    context = {"posts":posts, "form":form}
    return render (request, "social/feed.html", context)

def deletarPublicacao(request,id):
    post = Publicacao.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('social:feed')

    context = {'post':post}
    return render(request,'social/deletar-post.html',context)


def editarPublicacao(request,id):
    post = Publicacao.objects.get(id=id)
    form = Publicacao_form(instance=post)
    if request.method == 'POST':
        form = Publicacao_form(request.POST,instance=post)
        form.save()
        return redirect('social:feed')

    context = {'post':post,'form':form}
    return render(request,'social/editar-post.html',context)