from django.http import HttpResponse
from django.shortcuts import render
from post_machine import models
# Create your views here.

def post_machine_view(request):
    #return render(request, 'post_machine.html')
    return HttpResponse("hi, post_machine")


def one_post_machine_view(request, post_machine_id): # це def locker_view(request, machine_id):
    one_postmachine = models.PostMachine.objects.get(id=post_machine_id)
    postmachine_lockers = models.Locker.objects.filter(post_machine=one_postmachine)
    # коли треба відфільтрувати всі локери, які належать конкретному поштомату,
    # треба фільтрувати по конкретному поштомату(екземпляр класу), а не по id

    #one_locker = models.Locker.objects.get(pk=5)
    return HttpResponse(f'ok, {[itm.id for itm in postmachine_lockers]}')

    #return render(request, 'one_post_machine.html')
    #return HttpResponse("hi, one post_machine")


def locker_one_post_machine_view(request, post_machine_id, locker_id):
    # чому post_machine_id не треба передати параметром?!!!!!!!!!!
    #one_postmachine = models.PostMachine.objects.get(id=post_machine_id)
    one_locker = models.Locker.objects.get(id=locker_id) # можливо (pk=1)
    return HttpResponse(f'locker is {one_locker.status}')# статус комірки вивести

    #return render(request, 'box_one_post_machine.html')
    #return HttpResponse("hi, locker of some post_machine")


# def locker_view(request, machine_id): # = def one_post_machine_view(request, post_machine_id)
#     one_postmachine = models.PostMachine.objects.get(id=machine_id)
#     postmachine_lockers = models.Locker.objects.filter(post_machine=one_postmachine)
#
#     one_locker = models.Locker.objects.get(pk=5)
#     return HttpResponse(f'ok, {[itm.id for itm in postmachine_lockers]}')
