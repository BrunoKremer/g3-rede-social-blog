from django.shortcuts import render,redirect
from django.http import HttpResponse, request, response
from django.views import generic
from .models import Publicacao,Like
from django.urls.base import reverse_lazy
from .forms import Publicacao_form,Comentario_publi
from usuarios.models import CustomUser
from .models import Comment

# View feed, passamos o formulário de Publicação
# Data - passamos o model de Publicação
# Form - Passamos o formulário de Publicação
def feed(request):
    posts = Publicacao.objects.all()
    comentarios = Comment.objects.filter()
    
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
            data = Comment()
            data.comentario = form_comentario.cleaned_data['comentario']
            # data.foto = form_comentario.cleaned_data['foto']
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

def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Publicacao.objects.get(id=post_id)
        
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like , created = Like.objects.get_or_create(user=user,post_id=post_id)

        if not created:
            if like.value =='Like':
                like.value = 'Deslike'

            else:
                like.value = 'Like'

            like.save()

    return redirect('social:feed')

def Publi_detail(request, pk):
    comentarios = Comment.objects.filter()
    qtde = 0

    for q in comentarios:
        qtde = qtde + 1

    post = Publicacao.objects.get(pk=pk)
    

    context = {"post": post, 'comentarios':comentarios, 'qtde':qtde}
    return render (request, 'social/publi_detail.html', context)