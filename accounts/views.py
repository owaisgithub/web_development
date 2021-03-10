from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User, auth
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        name = request.POST['your_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        count = 0
        for i in password:
            count += 1

        if User.objects.filter(username=username).exists():
            messages.info(request, 'mobile number already exist')
            return redirect('/accounts/register')

        elif count < 8:
            messages.info(request, 'password should be 8 charecter')
            return redirect('/accounts/register')

        else:
            user = User.objects.create_user(first_name=name, username=username, email=email, password=password)
            user.save()
            print("User created")

            return render(request, 'complete.html')


    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'User does not exist')
            return redirect('/accounts/login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def forgotPassword(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            if password1 == password2:
                pass

    else:
        return render(request, 'forgotPassword.html')