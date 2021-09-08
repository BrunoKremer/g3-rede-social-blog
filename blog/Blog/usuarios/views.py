from usuarios.models import CustomUser
from django.db.models.base import Model
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

# class EditFormView(generic.CreateView):
#     form_class = UsuarioFormChange
#     template_name = "registration/profile.html"
#     success_url = reverse_lazy('usuarios:sucess')

# Create your views here.

class RegistradoView(generic.TemplateView):
    template_name = "registration/sucess.html"


# class ProfileView(generic.ListView ):
#     model = CustomUser
#     template_name = "registration/profile.html"


def ProfileView(request, pk):
    usuario = CustomUser.objects.get(pk=pk)
    return render (request, "registration/profile.html", { "user": usuario})