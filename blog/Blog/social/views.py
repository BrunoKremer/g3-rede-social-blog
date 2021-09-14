from django.shortcuts import render
from django.views import generic
from .models import Publicacao
from .forms import Feed_form
from django.urls.base import reverse_lazy

def feed(request):
    posts = Publicacao.objects.all()
    context = {"posts":posts}
    return render (request, "social/feed.html", context)
