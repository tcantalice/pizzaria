from django.db.models import Manager

from .querysets import ActiveQuerySet


class ActivableManager(Manager):
    def __init__(self, field_name='ativo'):
        super().__init__()
        self.field_name = field_name

    def get_queryset(self):
        return ActiveQuerySet(
            self.model, using=self._db, field_name=self.field_name
        )

    def ativos(self):
        return self.get_queryset().ativos()

    def inativos(self):
        return self.get_queryset().inativos()
