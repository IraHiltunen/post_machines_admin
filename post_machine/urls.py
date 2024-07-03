from django.urls import path

import post_machine.views

urlpatterns = [
    path('', post_machine.views.post_machine_view), # посилається на post_machine/views.py і буде її виконувати
    path('<int:post_machine_id>', post_machine.views.one_post_machine_view), # посилається на post_machine/views.py
    # і буде її виконувати
    path('<int:post_machine_id>/<int:box_id>', post_machine.views.box_one_post_machine_view)
]