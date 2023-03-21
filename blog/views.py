from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator


# Create your views here.


def BlogList(request):

    all_blogs = Blog.objects.all()
    blogs_paginator = Paginator(all_blogs, 20)
    page_number = request.GET.get('page')
    page_obj = blogs_paginator.get_page(page_number)

    context = {'blogs': page_obj}
    return render(request, 'blog/blog_list.html', context)


def BlogDetails(request, slug):
    blog_details = Blog.objects.get(slug=slug)
    context = {'blog': blog_details}
    return render(request, 'blog/blog_details.html', context)
