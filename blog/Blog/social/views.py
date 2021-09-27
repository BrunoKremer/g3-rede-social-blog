from django.shortcuts import render,redirect
from django.http import HttpResponse, request, response
from django.views import generic
from .models import Publicacao,Comentario
from django.urls.base import reverse_lazy
from .forms import Publicacao_form,Comentario_publi
from usuarios.models import CustomUser

# View feed, passamos o formulário de Publicação
# Data - passamos o model de Publicação
# Form - Passamos o formulário de Publicação
def feed(request):
    posts = Publicacao.objects.all()
    comentarios = Comentario.objects.all()
    
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
    context = {"posts":posts, "form":form,'comentarios':comentarios }
    return render (request, "social/feed.html", context)


# View para o usuário comentar alguma publicação
# Redireciona ele para uma página e quando ele realizar o comentário, volta para o FEED
# Data - Passamos o model Comentário
def comentar_Publicacao(request, id):
    post = Publicacao.objects.get(id = id)
    if request.method == 'POST':
        form_comentario = Comentario_publi(request.POST)
        if form_comentario.is_valid():
            data = Comentario()
            data.comentario = form_comentario.cleaned_data['comentario']
            data.foto = form_comentario.cleaned_data['foto']
            data.usuario_id = request.user.id
            data.publicacao_id = post.id
            data.save()
            return redirect('social:feed')
    else:
        form_comentario = Comentario_publi()
    context = {'post':post,"form_comentario":form_comentario}
    return render(request,'social/comentar_post.html',context)

# Função para deletar publicação, redireciona o usuário para uma página onde ele pode deletar a publicação
def deletarPublicacao(request,id):
    post = Publicacao.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('social:feed')

    context = {'post':post}
    return render(request,'social/deletar-post.html',context)

# Função para editar publicação, redireciona o usuário para uma página onde ele pode editar a publicação
# No form, está instanciado a publicação anterior e o usuário pode editar
def editarPublicacao(request,id):
    post = Publicacao.objects.get(id=id)
    form = Publicacao_form(instance=post)
    if request.method == 'POST':
        form = Publicacao_form(request.POST,instance=post)
        form.save()
        return redirect('social:feed')

    context = {'post':post,'form':form}
    return render(request,'social/editar-post.html',context)