from rest_framework import viewsets
from main.models import Post, Category, Indicacao
from main.api.serializers import PostSerializer, CategorySerializer, IndicacaoSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class IndicacaoViewSet(viewsets.ModelViewSet):
    serializer_class = IndicacaoSerializer
    queryset = Indicacao.objects.all()

