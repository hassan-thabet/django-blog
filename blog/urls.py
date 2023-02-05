from django.urls import path, include
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.BlogList),
    path('<str:slug>', views.BlogDetails, name='blog_details'),
]
