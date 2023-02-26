from .models import Blog
from .serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def bloglistapi(request):
    blogs_list = Blog.objects.all()
    data = BlogSerializer(blogs_list, many=True).data
    return Response({'data': data})
