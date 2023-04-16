from django.contrib import admin

from mymenu.models import Client, Menu


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'menu', ]
