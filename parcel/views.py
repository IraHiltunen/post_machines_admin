from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def parcels_view(request):
    #return render(request, 'parcel.html')
    return HttpResponse("hi, beauty parcels")


def one_parcel_view(request, parcel_id):
    #return render(request, 'one_parcel.html')
    return HttpResponse("hi, beauty one parcels")

