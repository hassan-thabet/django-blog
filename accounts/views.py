import sys
from django.shortcuts import render, redirect
from .forms import SignupForm  # , LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.


def signup(request):

    if request.method == "POST":
        form = SignupForm(request.POST)
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/accounts/profile')
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {form: form})


# def login(request):

#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         username = form.cleaned_data.get['username']
#         password = form.cleaned_data.get['password']
#         user = authenticate(username=username, password=password)
#         login(request, user)

#         return redirect('')
#     else:
#         form = LoginForm()

#     return render(request, 'registration/login.html', {form: "form"})
