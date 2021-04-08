from pizzaria.modules.core.models import DomainModel
from .config import DomainConfig

class _Meta(DomainModel.Meta):
    app_label = DomainConfig.module_label()

class Ingrediente(DomainModel):
    class Meta(_Meta):
        db_table = 'ingrediente'


class TipoBebida(DomainModel):
    class Meta(_Meta):
        db_table = 'tipo_bebida'


class TipoSabor(DomainModel):
    class Meta(_Meta):
        db_table = 'tipo_sabor'


class StatusPedido(DomainModel):
    class Meta(_Meta):
        db_table = 'status_pedido'

class Tamanho(DomainModel):
    class Meta(_Meta):
        db_table = 'tamanho'
