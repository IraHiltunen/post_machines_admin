from django.urls import path

import user.views

urlpatterns = [
    path('', user.views.user_page) # посилається на user.views.user_page і буде її виконувати
]