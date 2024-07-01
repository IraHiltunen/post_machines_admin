from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def user_page(request):
    HttpResponse("hello ira user page")