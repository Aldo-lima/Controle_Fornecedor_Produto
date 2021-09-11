from django.contrib import admin
from django.urls import path
from .views import fornecedores, novoFornecedor, fornecedorEditar, fornecedorVer, fornecedorDetete

urlpatterns = [
    path('fornecedores', fornecedores, name='listar_fornecedor'),
    path('novo_fornecedor', novoFornecedor, name='fornecedor_create'),
    path('ver_fornecedor/<int:id>', fornecedorVer, name='fornecedor_ver'),
    path('editar_fornecedor/<int:id>', fornecedorEditar, name='fornecedor_editar'),
    path('delete_fornecedores/<int:id>', fornecedorDetete, name='fornecedor_delete'),

]