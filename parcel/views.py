import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from parcel import models
from parcel.models import Parcel


# Create your views here.
def parcels_view(request):
    user = request.user
    parcels = models.Parcel.objects.filter(recipient=user)
    return render(request, 'parcels.html',
                  context={'parcels': parcels})

    #return HttpResponse("hi, parcels")
    #return render(request, 'parcels.html')


def get_parcel(request):
    if request.method == "POST":
        parcel = Parcel.objects.get(pk=request.POST['parcel_id'])
        parcel.status = True
        parcel.open_datetime = datetime.datetime.now()
        if parcel.order_datetime is None:
            parcel.order_datetime = datetime.datetime.now()
        if parcel.update_datetime is None:
            parcel.update_datetime = datetime.datetime.now()
        parcel.save()

        parcel.locker.status = True
        parcel.locker.save()
        return redirect("/parcel/")


def one_parcel_view(request, parcel_id):
    result = models.Parcel.objects.get(pk=parcel_id)
    return render(request, "one_parcel.html",
                  context={'parcel': result})

    #return HttpResponse(f"hi, one parcel: {result.sender}")# відображаю сендера
    #return render(request, 'one_parcel.html')
