from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def user_page(request):
    # return render(request, 'user_page.html')
    return HttpResponse("hello ira user page")