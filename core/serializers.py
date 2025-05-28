from rest_framework import serializers
from .models import Cidade, Fornecedor, FornecedorCelular

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = ['id', 'nome', 'uf']

class FornecedorCelularSerializer(serializers.ModelSerializer):
    class Meta:
        model = FornecedorCelular
        fields = ['id', 'numero']

class FornecedorSerializer(serializers.ModelSerializer):
    celulares = FornecedorCelularSerializer(many=True)
    cep = serializers.CharField(max_length=12, required=False, allow_blank=True)

    class Meta:
        model = Fornecedor
        fields = ['id', 'nome', 'cnpj', 'endereco', 'numero', 'bairro', 'cep', 'cidade', 'celulares']

    def create(self, validated_data):
        celulares_data = validated_data.pop('celulares', [])
        fornecedor = Fornecedor.objects.create(**validated_data)
        for celular_data in celulares_data:
            FornecedorCelular.objects.create(fornecedor=fornecedor, **celular_data)
        return fornecedor

    def update(self, instance, validated_data):
        celulares_data = validated_data.pop('celulares', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        instance.celulares.all().delete()
        for celular_data in celulares_data:
            FornecedorCelular.objects.create(fornecedor=instance, **celular_data)
        return instance

    def to_internal_value(self, data):
        # Corrige o erro do PUT quando o Postman envia uma lista
        if isinstance(data, list) and len(data) == 1 and isinstance(data[0], dict):
            data = data[0]
        return super().to_internal_value(data)
