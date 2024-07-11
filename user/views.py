from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/user/')
        else:
            context['error'] = "invalid username or password"
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('/login/')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        user = User.objects.create_user(username=username, email=email, password=password,
                                        first_name=first_name, last_name=last_name)
        user.save()
        return redirect('/login/')
    else:
        return render(request, 'register.html')  # якщо context нема, то можна не писати його


@login_required
def user_page(request):
    return render(request, 'user_page.html', context={'username': request.user.username,
                                                      'email': request.user.email})
    return HttpResponse("hello ira user page")