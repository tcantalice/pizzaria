from django.db import models

from .managers import ActivableManager

class ActivableModel(models.Model):
    ativo = models.BooleanField(default=True)
    objects = ActivableManager()

class DomainModel(models.Model):
    descricao = models.CharField(length=45)
