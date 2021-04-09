from django.db import models

from pizzaria.modules.core.models import ActivableModel, DomainModel

from .config import ProductConfig


class _Meta:
    app_label = ProductConfig.module_label()


class Sabor(ActivableModel):
    descricao = models.CharField(max_length=45)
    tipo = models.ForeignKey(
        ProductConfig.model_label('TipoSabor'), on_delete=models.RESTRICT
    )
    ingredientes = models.ManyToManyField(
        ProductConfig.model_label('Ingrediente'), db_table='sabor_ingrediente'
    )

    class Meta(_Meta, ActivableModel.Meta):
        db_table = 'sabor'


class Ingrediente(DomainModel):
    class Meta(_Meta, DomainModel.Meta):
        db_table = 'ingrediente'


class TipoBebida(DomainModel):
    class Meta(_Meta, DomainModel.Meta):
        db_table = 'tipo_bebida'


class TipoSabor(DomainModel):
    tamanhos = models.ManyToManyField(
        ProductConfig.model_label('Tamanho'),
        through=ProductConfig.model_label('Preco')
    )

    class Meta(_Meta, DomainModel.Meta):
        db_table = 'tipo_sabor'


class Tamanho(DomainModel):
    tipos_sabores = models.ManyToManyField(
        ProductConfig.model_label('TipoSabor'),
        through=ProductConfig.model_label('Preco')
    )

    class Meta(_Meta, DomainModel.Meta):
        db_table = 'tamanho'


class Preco(models.Model):
    tipo_sabor = models.ForeignKey(
        ProductConfig.model_label('TipoSabor'),
        on_delete=models.CASCADE,
        related_name='precos'
    )
    tamanho = models.ForeignKey(
        ProductConfig.model_label('Tamanho'),
        on_delete=models.CASCADE,
        related_name='precos'
    )
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta(_Meta):
        db_table = 'preco'
