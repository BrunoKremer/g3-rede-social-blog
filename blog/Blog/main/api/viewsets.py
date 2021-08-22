from rest_framework import viewsets
from main.models import Post, Categoria, Indicacao
from main.api.serializers import PostSerializer, CategoriaSerializer, IndicacaoSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()

class IndicacaoViewSet(viewsets.ModelViewSet):
    serializer_class = IndicacaoSerializer
    queryset = Indicacao.objects.all()

