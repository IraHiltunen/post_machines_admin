from django.urls import path

import post_machine.views

urlpatterns = [
    path('', post_machine.views.post_machine_view), # посилається на post_machine_view і буде її виконувати
    path('<post_machine_id>', post_machine.views.one_post_machine_view), # посилається на post_machine_view
    # і буде її виконувати
   # path('<post_machine_id>'/'<box_id>', post_machine.view.box_one_post_machine_view)
]