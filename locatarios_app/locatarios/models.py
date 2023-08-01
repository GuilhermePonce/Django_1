from django.db import models

class Locatario(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome