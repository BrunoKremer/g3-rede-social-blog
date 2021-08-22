from rest_framework.serializers import ModelSerializer
from main.models import Post, Categoria, Indicacao

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class IndicacaoSerializer(ModelSerializer):
    class Meta:
        model = Indicacao
        fields = '__all__'
