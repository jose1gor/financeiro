from core.models import Fornecedor

class FornecedorRepository:
    @staticmethod
    def get_by_id(fornecedor_id):
        return Fornecedor.objects.get(id=fornecedor_id)

    @staticmethod
    def create(**kwargs):
        return Fornecedor.objects.create(**kwargs)

    @staticmethod
    def update(instance, **kwargs):
        for attr, value in kwargs.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    @staticmethod
    def delete(instance):
        instance.delete()

    @staticmethod
    def list_all():
        return Fornecedor.objects.all()
