from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'
