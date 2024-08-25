from django.db import models


class Capital(models.Model):
    nome = models.CharField(max_length=255)
    pais = models.OneToOneField('Paises', on_delete=models.CASCADE, related_name='capital')
    
    def __str__(self):
        return self.nome


class Paises(models.Model):
    nome = models.CharField(max_length=255)
    populacao = models.IntegerField()
    regiao = models.CharField(max_length=255)
    subregiao = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome
    
