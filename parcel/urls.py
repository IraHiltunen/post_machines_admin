from django.urls import path

import parcel.views

urlpatterns = [
    path('', parcel.views.parcels_view), # посилається на parcel.views.parcels_view і буде її виконувати
    path('get_parcel/', parcel.views.get_parcel),
    path('<parcel_id>/', parcel.views.one_parcel_view)
    # посилається на parcel/views.py def one_parcel_view і буде її виконувати
]