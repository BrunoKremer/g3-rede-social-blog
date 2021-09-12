from usuarios.models import CustomUser
from django.db.models.base import Model
from django.shortcuts import  render, redirect
from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView
from .forms import UsuarioForm, UsuarioFormChange
 
class CadastroFormView(generic.CreateView):
    form_class = UsuarioForm
    template_name = "registration/cadastro.html"
    success_url = reverse_lazy('usuarios:sucess')

class RegistradoView(generic.TemplateView):
    template_name = "registration/sucess.html"

class FeedView(generic.TemplateView):
    template_name = "social/feed.html"

def ProfileView(request, pk):
    usuario = CustomUser.objects.get(pk=pk)
    return render (request, "registration/profile.html", { "user": usuario})

class UserChange(generic.UpdateView):
    model = CustomUser
    form_class = UsuarioFormChange
    template_name = 'registration/edit_user.html'
    success_url = reverse_lazy('usuarios:feed')