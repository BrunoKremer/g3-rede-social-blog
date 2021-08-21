from rest_framework.serializers import ModelSerializer
from main.models import Post, Category, Indicacao

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class IndicacaoSerializer(ModelSerializer):
    class Meta:
        model = Indicacao
        fields = '__all__'
