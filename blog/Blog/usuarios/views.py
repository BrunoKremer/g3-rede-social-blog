from .models import CustomUser
from django.db.models.base import Model
from django.shortcuts import  get_list_or_404, render, redirect, get_object_or_404
from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView
from .forms import UsuarioForm, UsuarioFormChange
from Contato.enviar_email import enviar_email_via_gmail
from social.models import Publicacao
from django.contrib.auth.models import User
from django.http import HttpResponse


 
#  View para cadastrar os usuários
class CadastroFormView(generic.CreateView):
    form_class = UsuarioForm
    template_name = "registration/cadastro.html"
    success_url = reverse_lazy("usuarios:sucess")

# View que redireciona para página de sucesso no cadastro
class RegistradoView(generic.TemplateView):
    template_name = "registration/sucess.html"

# View do perfil de usuário, pk seria o id do user
def ProfileView(request, pk):
    usuario = CustomUser.objects.get(pk=pk)
    email = usuario.email   
    enviar_email_via_gmail('Bem-vindo à InfoCode', "teste", email)
    
    return render (request, "registration/profile.html", { "user": usuario})

# View para editar informações do usuário
class UserChange(generic.UpdateView):
    model = CustomUser
    form_class = UsuarioFormChange
    template_name = 'registration/edit_user.html'
    success_url = reverse_lazy("social:feed")
    

def seguir_usuario(request, id):
    request.user.seguidores.add(get_object_or_404(CustomUser, id=id))
    return redirect("social:feed")




    