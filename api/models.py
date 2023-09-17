#from tkinter import CASCADE
import hashlib
from django.db import models
import string
import random

def sha256Encode(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=15, null= False, default ="")
    surname = models.CharField(max_length=15, null=False, default="")
    user = models.CharField(max_length=12, null = False, default="")
    password = models.CharField(max_length=12, null = False, default="")
    canUpload = models.BooleanField(default=True)
    canDownload = models.BooleanField(default = False)
