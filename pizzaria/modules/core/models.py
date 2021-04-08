from django.db import models

from .managers import ActivableManager
from .config import CoreConfig


class _Meta:
    app_label = CoreConfig.module_label()


class ActivableModel(models.Model):
    ativo = models.BooleanField(default=True)
    objects = ActivableManager()

    class Meta(_Meta):
        abstract = True


class DomainModel(models.Model):
    descricao = models.CharField(max_length=45)

    class Meta(_Meta):
        abstract = True
        ordering = ('descricao',)
