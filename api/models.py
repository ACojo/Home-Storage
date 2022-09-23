#from tkinter import CASCADE
from django.db import models
import string
import random


def gen_code():
    length = 6

    while True:
        id = ''.join(random.choices(string.ascii_uppercase, k = length))
        if Bilet.objects.filter(code = id).count() == 0:
            break
    return id

# Create your models here.
class Persoana(models.Model):
    name = models.CharField(max_length=15, null= False, default ="")
    surname = models.CharField(max_length=15, null=False, default="")
    id_card = models.CharField(max_length=12, null = False, default="", unique=True)


class Bilet(models.Model):
    code = models.CharField(max_length= 8, default=gen_code, unique = True)
    price = models.IntegerField(null = False)
    start_station = models.CharField(max_length=16)
    stop_station = models.CharField(max_length=16)
    current_time = models.DateTimeField(auto_now_add= True)
    #id_persoana = models.ForeignKey("Persoana", on_delete=models.CASCADE, default= -1)

