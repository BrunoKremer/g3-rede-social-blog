
from django.views.generic.edit import FormView
from .forms import ComentariosForm
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.http import HttpResponse, request, response
from django.db.models import Q
from .models import Indicacao, Post, Categoria, Comentarios, Curtir
from django.core.paginator import Paginator
from django.views import generic
from django.urls import reverse_lazy

# Função para página principal
# * cat é o filtro que fazemos por categoria, nome
# * paginator é a paginação

def home(request):
    cat = ''

    if request.GET.get('cat'):
        cat = request.GET.get('cat')
        
    categorias = Categoria.objects.filter(categoria__icontains=cat) 
    post =  Post.objects.distinct().filter(
        Q(titulo__icontains=cat)| 
        Q(subtitulo__icontains=cat)|
        Q(categoria__in=categorias)
    )
    paginator = Paginator(post, 5) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categoria =  Categoria.objects.all()
    

    context = {'post':post, 'categoria':categoria, 'page_obj': page_obj,'cat':cat}
    
    return render(request, 'blog/home.html', context )

# View de Posts detalhados pela ID
#  * qtde pega a quantidade de comentários do post

def PostDetailView(request, pk):
    post = get_object_or_404(Post,pk=pk)
    comentarios = Comentarios.objects.filter()
    qtde = 0

    for q in comentarios:
        qtde = qtde + 1

    
    if request.method == 'POST':
        form = ComentariosForm(request.POST)
        if form.is_valid():
            data = Comentarios()
            data.usuario_id = request.user.id
            data.comentario = form.cleaned_data['comentario']
            data.post_id = pk
            data.save()
    else:
        form = ComentariosForm()

    context = {"post": post, 'form':form, 'comentarios':comentarios, 'qtde':qtde}
    return render (request, 'blog/post_detail.html', context)

def curtir_post(request):
    usuario = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)

        if usuario in post_obj.curtidas.all():
            post_obj.curtidas.remove(usuario)
        else:
            post_obj.curtidas.add(usuario)
        
        curtir, created = Curtir.objects.get_or_create(usuario=usuario,post_id=post_id)

        if not created:
            if curtir.avaliacao == 'Gostei':
                curtir.avaliacao = 'Não Gostei'
            else:
                curtir.avaliacao = 'Gostei'
        
        curtir.save()

    return redirect('main:indicacao')
   
   
# View para todas indicações

def indicacao(request):
    indicacao = get_list_or_404(Indicacao)
    context = {'indicacao':indicacao}
    return render(request, 'blog/indicacao.html', context)

# Indicação detalhada, escolhida pelo usuário pela ID

class IndicacaoDetailView(generic.DetailView):
    model = Indicacao
    template_name = 'blog/indicacao_detail.html'

