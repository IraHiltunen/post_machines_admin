from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def post_machine_view(request):
    #return render(request, 'post_machine.html')
    return HttpResponse("hi, beauty post_machine")


def one_post_machine_view(request, post_machine_id):
    #return render(request, 'one_post_machine.html')
    return HttpResponse("hi, beauty one post_machine")


def box_one_post_machine_view(request, post_machine_id, box_id):
    #return render(request, 'box_one_post_machine.html')
    return HttpResponse("hi, beauty box one post_machine")