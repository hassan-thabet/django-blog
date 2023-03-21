from .models import Blog
from .models import Category
from .serializers import BlogSerializer
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination


# @api_view(['GET'])
# def bloglistapi(request):
#     blogs_list = Blog.objects.all()
#     data = BlogSerializer(blogs_list, many=True).data
#     return Response({'data': data})
# 

paginator = PageNumberPagination()


@api_view(['GET'])
def bloglistapi(request):
    blogs_list = Blog.objects.all()
    context = paginator.paginate_queryset(blogs_list , request)
    data = BlogSerializer(context, many=True).data
    return paginator.get_paginated_response(data)




@api_view(['GET'])
def blogdetailsapi(request, id):
    blog_details = Blog.objects.get(id=id)
    data = BlogSerializer(blog_details).data

    # incrrease popularty counter every request
    blog_details.popular += 1
    blog_details.save()

    # return json data
    return Response({'data': data})


@api_view(['GET'])
def categoryblogsapi(request, category_id):

    category_blogs = Blog.objects.filter(category=category_id)
    context = paginator.paginate_queryset(category_blogs , request)
    data = BlogSerializer(context, many=True).data
    return paginator.get_paginated_response(data)


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
    context = paginator.paginate_queryset(recent_articles , request)
    data = BlogSerializer(context, many=True).data
    return paginator.get_paginated_response(data)


# ===================================================================================


@api_view(['GET'])
def popularArticlesapi(request):
    popular_articles = Blog.objects.order_by('-popular')
    context = paginator.paginate_queryset(popular_articles , request)
    data = BlogSerializer(context, many=True).data
    return paginator.get_paginated_response(data)


#  ====================================================================================


@api_view(['GET'])
def shortArticlesapi(request):
    short_articles = Blog.objects.order_by('read_time')
    context = paginator.paginate_queryset(short_articles , request)
    data = BlogSerializer(context, many=True).data
    return paginator.get_paginated_response(data)


#  ====================================================================================


@api_view(['GET'])
def randomArticlesapi(request):
    random_articles = Blog.objects.order_by('updated_at')
    context = paginator.paginate_queryset(random_articles , request)
    data = BlogSerializer(context, many=True).data
    return paginator.get_paginated_response(data)


#  ====================================================================================

# from rest_framework.pagination import PageNumberPagination


# @api_view(['GET',])
# def my_function_based_list_view(request):
#     paginator = PageNumberPagination()
#     query_set = MyModel.objects.all()
#     context = paginator.paginate_queryset(query_set, request)
#     serializer = MyModelSerializer(context, many=True)
#     return paginator.get_paginated_response(serializer.data)