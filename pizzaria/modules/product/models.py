from django.db import models

from pizzaria.modules.core.models import ActivableModel
from pizzaria.modules.domain.models import TipoSabor, Ingrediente

from .config import ProductConfig

class _Meta:
    app_label = ProductConfig.module_label()


class Sabor(ActivableModel):
    descricao = models.CharField(max_length=45)
    tipo = models.ForeignKey(TipoSabor, on_delete=models.RESTRICT)
    ingredientes = models.ManyToManyField(Ingrediente, db_table='sabor_ingrediente')

    class Meta(_Meta, ActivableModel.Meta):
        db_table = 'sabor'

