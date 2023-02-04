from django.urls import path , include
from . import views
urlpatterns = [
    path('', views.AllBlogs),
    path('<int:id>', views.BlogDetails),
]

