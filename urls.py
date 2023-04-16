"""menu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from mymenu.views import create_Menu, create_Client, list_Menu, list_Client, show_omlet_view, show_buter_view, \
    show_pasta_view, dishes_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', create_Menu),
    path('client/', create_Client),
    path('list_menu/', list_Menu),
    path('list_client/', list_Client),


    path('', dishes_view, name='dishes'),
    path('omlet/', show_omlet_view, name='omlet'),
    path('buter/', show_buter_view, name='buter'),
    path('pasta/', show_pasta_view, name='pasta'),
]
