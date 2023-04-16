from django.db import models

class Menu(models.Model):
    menu = models.CharField('Название', max_length=50)
    position = models.PositiveIntegerField('Позиция', default=1)

    def __str__(self):
        return self.menu

class Client(models.Model):
    name = models.CharField('Имя клиента', max_length=150)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name