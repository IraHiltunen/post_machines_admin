"""
URL configuration for post_machines_admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import user.views

urlpatterns = [
    path('admin/', admin.site.urls),# за замовченням
    path('user/', user.views.user_page), # user посилається на user.views.user_page)
    path('parcel/', include('parcel.urls')), # parsel посилається на include('parcel.urls')... треба включити усі
# штук,які є в 'parcel.urls'
    path('post_machine/', include('post_machine.urls'))
]
