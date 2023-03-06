from .models import Blog
from .models import Category
from .serializers import BlogSerializer
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import random


@api_view(['GET'])
def bloglistapi(request):
    blogs_list = Blog.objects.all()
    data = BlogSerializer(blogs_list, many=True).data
    return Response({'data': data})


@api_view(['GET'])
def blogdetailsapi(request, id):
    blog_details = Blog.objects.get(id=id)
    data = BlogSerializer(blog_details).data
    ## incrrease popularty counter every request
    blog_details.popular += 1
    blog_details.save()
    ## return json data
    return Response({'data': data})


@api_view(['GET'])
def categoryblogsapi(request, category_id):

    category_blogs = Blog.objects.filter(category=category_id)
    data = BlogSerializer(category_blogs, many=True).data
    return Response({'data': data})


#  ====================================================================================

@api_view(['GET'])
def categorylistapi(request):
    category_list = Category.objects.all()
    data = CategorySerializer(category_list, many=True).data
    return Response({'data': data})

#  ====================================================================================


@api_view(['GET'])
def recentArticlesapi(request):
    recent_articles = Blog.objects.order_by('-created_at')
    data = BlogSerializer(recent_articles, many=True).data
    return Response({'data': data})


# ===================================================================================


@api_view(['GET'])
def popularArticlesapi(request):
    popular_articles = Blog.objects.order_by('-popular')
    data = BlogSerializer(popular_articles, many=True).data
    return Response({'data': data})


#  ====================================================================================


@api_view(['GET'])
def shortArticlesapi(request):
    short_articles = Blog.objects.order_by('read_time')
    data = BlogSerializer(short_articles, many=True).data
    return Response({'data': data})


#  ====================================================================================


@api_view(['GET'])
def randomArticlesapi(request):
    random_articles = list(Blog.objects.all())
    random_items = random.sample(random_articles, 3)
    data = BlogSerializer(random_items, many=True).data
    return Response({'data': data})


#  ====================================================================================


@api_view(['GET'])
def searchArticleapi(request):
    blog_details = Blog.objects.all()
    data = BlogSerializer(blog_details).data

    ## return json data
    return Response({'data': data})