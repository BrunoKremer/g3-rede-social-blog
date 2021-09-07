from django.shortcuts import  render, redirect
from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView
 
# Relative import of GeeksForm
from .forms import UsuarioForm
 
class CadastroFormView(generic.CreateView):
    form_class = UsuarioForm
    template_name = "registration/cadastro.html"
    success_url = reverse_lazy('usuarios:sucess')

# Create your views here.

class RegistradoView(generic.TemplateView):
    template_name = "registration/sucess.html"
