from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        pwd = request.POST['password']

        if username == "" or username == " ":
            messages.info(request, 'Please Enter a Valid Username')
            return redirect('login')

        if pwd == "" or pwd == " ":
            messages.info(request, 'Please Enter a Valid Password')
            return redirect('login')

        user = auth.authenticate(username=username, password=pwd)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials!')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
