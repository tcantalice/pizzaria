from pizzaria.modules.core.models import DomainModel

class Ingrediente(DomainModel):
    class Meta:
        db_table = 'ingrediente'


class TipoBebida(DomainModel):
    class Meta:
        db_table = 'tipo_bebida'


class TipoSabor(DomainModel):
    class Meta:
        db_table = 'tipo_sabor'


class StatusPedido(DomainModel):
    class Meta:
        db_table = 'status_pedido'

class Tamanho(DomainModel):
    class Meta:
        db_table = 'tamanho'
