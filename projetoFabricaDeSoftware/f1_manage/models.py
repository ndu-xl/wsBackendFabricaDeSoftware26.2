from django.db import models

# Create your models here.
class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    def __str__(self):
        return self.nome


class Piloto(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.IntegerField()

    equipe = models.ForeignKey(
        Equipe,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )