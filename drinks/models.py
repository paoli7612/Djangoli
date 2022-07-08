from django.db import models

# Create your models here.

class Drink(models.Model):
    nome = models.CharField(max_length=64)
    immagine = models.ImageField()
    prezzo = models.FloatField()

    def __str__(self):
        return self.nome