from django.db import models
from fornecedor.models import Fornecedor
# Create your models here.

UNIDADE_DE_MEDIDA = (
     ('unidade', 'Unidade'),
     ('kilo', 'Kilo'),
     ('litro', 'Litro'),

   )


class Produto(models.Model):
    produto = models.CharField('Nome', max_length=100, unique=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    descricao = models.CharField('Descrição', max_length=200)
    unidade_medida = models.CharField('Unidade de medida', max_length=11, choices=UNIDADE_DE_MEDIDA)
    quantidade_embalagem = models.IntegerField('Qantidade na embalagem')
    preco = models.DecimalField('preço', max_digits=7, decimal_places=2)

    class Meta:
        ordering = ('produto',)

    def __str__(self):
        return self.produto
