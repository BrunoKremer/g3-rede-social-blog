
from django.views.generic.edit import FormView
from .forms import FormComentario
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
    paginator = Paginator(post, 5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categoria =  Categoria.objects.all()
    

    context = {'post':post, 'categoria':categoria, 'page_obj': page_obj,'cat':cat}
    
    return render(request, 'blog/home.html', context )
        

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class ComentarioView(FormView):
    form_class = FormComentario
    success_url = reverse_lazy('post_detail')
    template_name = 'blog/post_detail.html'

    def form_valid(self, form, *args, **kwargs):
        comentario = form.cleaned_data['comentario']
        comentario.save()
        return super().form_valid(form)



    




# Create your views here.

            
