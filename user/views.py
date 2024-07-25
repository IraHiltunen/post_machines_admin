from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from user.forms import LoginForm, RegisterForm


# class LoginView(View):
#
#     def get(self, request):
#         return render(request, "login.html")
#
#     def post(self, request):
#         username = request['username']
#         password = request['password']
#         user = authenticate(request, username=username, password=password)
#         if user is None:
#             context['error'] = "invalid username or password"
#             return render(request, 'login.html', context=context)
#         else:
#             login(request, user)
#             return redirect('/user/')

def login_view(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/user/')
        context['error'] = "invalid username or password"
    context['form'] = LoginForm()
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('/login/')


# class RegisterView(View):
#
#     def get(self, request):
#         return render(request, "register.html")
#
#     def post(self, request):
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         first_name = request.POST['first_name']  # why first_name,but not firstname
#         last_name = request.POST['last_name']
#         user = User.objects.create_user(username=username,
#                                         email=email,
#                                         password=password,
#                                         firstname=first_name,
#                                         lastname=last_name)
#         user.save()
#         return redirect('/login/')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'],
                                            first_name=form.cleaned_data['first_name'],
                                            last_name=form.cleaned_data['last_name'])
            user.save()
            return redirect('/login/')
    else:
        return render(request, 'register.html',
                      context={'form': RegisterForm()})  # якщо context нема, то можна не писати його


@login_required
def user_page(request):
    return render(request, 'user_page.html',
                  context={'username': request.user.username,
                           'email': request.user.email})