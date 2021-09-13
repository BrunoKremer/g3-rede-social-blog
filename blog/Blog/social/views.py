from django.shortcuts import render
from django.views import generic
from .models import Publicacao


def feed(request):
    posts = Publicacao.objects.all()
    context = {"posts":posts}
    return render (request, "social/feed.html", context)

# class FeedView(generic.TemplateView):
#     template_name = "social/feed.html"
