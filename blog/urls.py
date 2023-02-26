from django.urls import path, include
from . import views
from . import api

app_name = "blog"
urlpatterns = [

    path('', views.BlogList),
    path('<str:slug>', views.BlogDetails, name='blog_details'),


    # API URLS

    path('api/blog_list', api.bloglistapi, name='blog_list_api'),
    path('api/blog_details/<int:id>', api.blogdetailsapi, name='blog_details_api'),
]
