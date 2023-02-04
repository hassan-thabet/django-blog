from django.shortcuts import render
from .models import Blog

# Create your views here.


def BlogList(request):

    all_blogs = Blog.objects.all()
    context = {'blogs': all_blogs}
    return render(request, 'blog/blog_list.html', context)


def BlogDetails(request, id):
    blog_details = Blog.objects.get(id=id)
    context = {'blog': blog_details}
    return render(request, 'blog/blog_details.html', context)
