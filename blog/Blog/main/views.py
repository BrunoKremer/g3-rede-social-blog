
from django.views.generic.edit import FormView
from .forms import ComentariosForm
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.http import HttpResponse, request, response
from django.db.models import Q
from .models import Indicacao, Post, Categoria, Comentarios
from django.core.paginator import Paginator
from django.views import generic
from django.urls import reverse_lazy

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


def PostDetailView(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = ComentariosForm()
        if form.is_valid():
            form.save()
    else:
        form = ComentariosForm()
    return render (request, 'blog/post_detail.html', { "post": post, 'form':form})

# class PostDetailView(generic.DetailView):
#     model = Post
#     form_class = ComentariosForm
#     template_name = 'blog/post_detail.html'

# class ComentarioView(FormView):
#     form_class = FormComentario
#     success_url = reverse_lazy('post_detail')
#     template_name = 'blog/post_detail.html'

    # def form_valid(self, form, *args, **kwargs):
    #     comentario = form.cleaned_data['comentario']
    #     comentario.save()
    #     return super().form_valid(form)
        

def indicacao(request):
    indicacao = get_list_or_404(Indicacao)
    context = {'indicacao':indicacao}
    return render(request, 'blog/indicacao.html', context)

class IndicacaoDetailView(generic.DetailView):
    model = Indicacao
    template_name = 'blog/indicacao_detail.html'

    




# Create your views here.

            
