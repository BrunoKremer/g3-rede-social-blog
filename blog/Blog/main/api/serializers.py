from rest_framework.serializers import ModelSerializer
from main.models import Post, Category

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
