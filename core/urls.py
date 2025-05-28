from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FornecedorViewSet, CidadeViewSet

router = DefaultRouter()
router.register(r'fornecedores', FornecedorViewSet)
router.register(r'cidades', CidadeViewSet)

urlpatterns = router.urls
