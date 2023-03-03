from rest_framework import serializers
from .models import Blog
from .models import Category


class BlogSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source="category.name", read_only=True)
    category_id = serializers.CharField(source="category.id", read_only=True)

    class Meta:
        model = Blog
        exclude = ('category',)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
