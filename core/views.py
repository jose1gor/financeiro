import requests
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Fornecedor, Cidade
from .serializers import FornecedorSerializer, CidadeSerializer
from .repository import FornecedorRepository

class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        cnpj = data.get('cnpj')
        if cnpj:
            endereco_info = self.get_endereco_by_cnpj(cnpj)
            if endereco_info:
                data.update(endereco_info)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        fornecedor = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = request.data.copy()
        cnpj = data.get('cnpj')
        if cnpj:
            endereco_info = self.get_endereco_by_cnpj(cnpj)
            if endereco_info:
                data.update(endereco_info)
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        fornecedor = serializer.save()
        return Response(serializer.data)

    def get_endereco_by_cnpj(self, cnpj):
        url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return {
                    'endereco': data.get('logradouro', ''),
                    'numero': data.get('numero', ''),
                    'bairro': data.get('bairro', ''),
                    'cep': data.get('cep', ''),
                }
        except Exception:
            pass
        return None
