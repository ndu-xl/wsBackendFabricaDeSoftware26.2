from django.db import models

# Create your models here.
class Piloto(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.IntegerField()