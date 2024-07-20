from django.urls import path

import post_machine.views

urlpatterns = [
    path('', post_machine.views.post_machine_view), # посилається на post_machine/views.py і буде її виконувати

    path('<int:post_machine_id>/', post_machine.views.one_post_machine_view), # посилається на post_machine/views.py
    # і буде її виконувати
    path('<int:post_machine_id>/<int:locker_id>/', post_machine.views.locker_one_post_machine_view)
]
# можливо тут / треба в кінці кожного ..._id