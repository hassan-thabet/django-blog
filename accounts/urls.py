from django.urls import path, include
from . import views

app_name = "accounts"
urlpatterns = [
    path('sign_up', views.signup, name='signup'),

]
