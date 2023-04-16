from django.shortcuts import render
from django.http import HttpResponse
from mymenu import models
from mymenu.models import Menu, Client


def create_Menu(request):
    menu = Menu(
        dish_1=request.GET.get('Название_блюда_1'),
        dish_2=request.GET.get('Название_блюда_2'),
        dish_3=request.GET.get('Название_блюда_3'),
    )
    menu.save()
    return HttpResponse(f'Создан список блюд.')

def list_Menu(request):
    menu_objects = Menu.objects.all()
    menu = [f'{menu_objects.id}, {menu_objects.dish_1}, {menu_objects.dish_2}, {menu_objects.dish_3}' for menu in menu_objects]
    return HttpResponse('<br>'.join(menu), print(f'Все товары: {menu}'))

def create_Client(request):
    client = Client(
        name=request.GET.get('Имя_клиента'),
    )
    client.save()
    return HttpResponse(f'Зарегистрирован_новый_клиент: {client.name}')

def list_Client(request):
    client_objects = Client.objects.all()
    clients = [f'{client.id}, {client.name}' for client in client_objects]
    return HttpResponse('<br>'.join(clients), print(f'Все клиенты: {clients}'))

def dishes_view(request):
    return render(request, 'dishes.html')


def show_omlet_view(request):

    servings = int(request.GET.get("servings", 1))

    omlet = {
        'eggs': [2],
        'milk': [0.1],
        'salt': [0.5]
    }

    print(f'На одну порцию: {omlet}')

    if servings:
        for i in omlet.keys():
            omlet[i] = [servings * x for x in omlet[i]]

    print(f'На {servings} порции: {omlet}')

    data = {'omlet': omlet}
    return render(request, 'omlet.html', context=data)


def show_pasta_view(request):

    servings = int(request.GET.get("servings", 1))

    pasta = {
        'pasta': [0.3],
        'cheese': [0.05]
    }

    if servings:
        for i in pasta.keys():
            pasta[i] = [servings * x for x in pasta[i]]
        print(f'На {servings} порции: {pasta}')

    data = {'pasta': pasta}
    return render(request, 'pasta.html', context=data)

def show_buter_view(request):

    servings = int(request.GET.get("servings", 1))

    buter = {
        'bread': [1],
        'sausage': [1],
        'cheese': [1],
        'tomato': [1],
    }

    if servings:
        for i in buter.keys():
            buter[i] = [servings * x for x in buter[i]]
        print(f'На {servings} порции: {buter}')

    return render(request, 'buter.html', {'context': buter})