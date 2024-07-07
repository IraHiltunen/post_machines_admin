from django.http import HttpResponse
from django.shortcuts import render
from parcel import models

# Create your views here.
def parcels_view(request):
    #return render(request, 'parcel.html')
    return HttpResponse("hi, parcels")


def one_parcel_view(request, parcel_id):
    #return render(request, 'one_parcel.html')
    result = models.Parcel.objects.get(pk=parcel_id)
    return HttpResponse(f"hi, one parcel: {result.sender}")# відображаю сендера

