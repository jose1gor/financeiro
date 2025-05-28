from django.contrib import admin
from .models import Cidade, Fornecedor, FornecedorCelular

# Register your models here.
admin.site.register(Cidade)
admin.site.register(Fornecedor)
admin.site.register(FornecedorCelular)
