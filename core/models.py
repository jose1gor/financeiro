from django.db import models

# Create your models here.

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome} ({self.uf})"

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=20, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    cep = models.CharField(max_length=12, blank=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class FornecedorCelular(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, related_name='celulares', on_delete=models.CASCADE)
    numero = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.fornecedor.nome} - {self.numero}"
