from django.http import HttpResponse
from django.shortcuts import render
from post_machine import models


def post_machine_view(request):
    post_machines = models.PostMachine.objects.all()
    return render(request, 'post_machines.html',
                  context={'post_machines': post_machines})
    #return HttpResponse("hi, post_machine")


def one_post_machine_view(request, post_machine_id): # це def locker_view(request, machine_id):
    one_postmachine = models.PostMachine.objects.get(id=post_machine_id)
    post_machine_lockers = models.Locker.objects.filter(post_machine=one_postmachine)

    # коли треба відфільтрувати всі локери, які належать конкретному поштомату,
    # треба фільтрувати по конкретному поштомату(екземпляр класу), а не по id
    # post_machine беру з post_machine/models.py з класу локер

    return render(request, 'one_post_machine.html',
                  context={'one_postmachine': one_postmachine,
                           'post_machine_lockers': post_machine_lockers})


    #one_locker = models.Locker.objects.get(pk=5)
    #return HttpResponse(f'ok, {[itm.id for itm in postmachine_lockers]}')


def locker_one_post_machine_view(request, post_machine_id, locker_id):
    # чому post_machine_id не треба передати параметром?- у нас усі комірkи по порядку ідуть

    one_postmachine = models.PostMachine.objects.get(id=post_machine_id)
    lockers = one_postmachine.locker_set.all()
    one_locker = models.Locker.objects.get(id=locker_id)
    return render(request, 'locker.html',
                  context={'one_locker': one_locker,
                           'one_post_machine': post_machine_id,
                           'lockers': lockers,
                           'one_postmachine': one_postmachine})
                  #'one_postmachine': one_postmachine тепер не потрібно


    #return HttpResponse(f'locker is {one_locker.status}')# статус комірки вивести
    #return render(request, 'box_one_post_machine.html')
    #return HttpResponse("hi, locker of some post_machine")

# def locker_view(request, machine_id): # example for def locker_one_post_machine_view
#     one_post_machine = models.PostMachine.objects.get(id=machine_id)
#     post_machine_locker = models.Locker.objects.filter(post_machine=one_post_machine)
#     lockers = one_post_machine.locker_set.all()
#     return render((request, 'locker2.html', {'machine_id': machine_id,
#                   'one_post_machine': one_post_machine,
#                   'post_machine_locker': post_machine_locker,
#                   'lockers': lockers}))


# def locker_view(request, machine_id): # = def one_post_machine_view(request, post_machine_id)
#     one_postmachine = models.PostMachine.objects.get(id=machine_id)
#     postmachine_lockers = models.Locker.objects.filter(post_machine=one_postmachine)
#
#     one_locker = models.Locker.objects.get(pk=5)
#     return HttpResponse(f'ok, {[itm.id for itm in postmachine_lockers]}')
