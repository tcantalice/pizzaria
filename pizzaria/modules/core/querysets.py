from django.db.models import QuerySet

class ActiveQuerySet(QuerySet):
    def __init__(
        self,
        model=None,
        query=None,
        using=None,
        hints=None,
        field_name='ativo',
    ):
        super().__init__(model=model, query=query, using=using, hints=hints)
        self.field_name = field_name

    def ativos(self):
        return self.filter(**{self.field_name: True})

    def inativos(self):
        return self.filter(**{self.field_name: False})
