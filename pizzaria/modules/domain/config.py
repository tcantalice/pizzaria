from django.apps import AppConfig
from django.apps.registry import apps

from pizzaria.bootstrap import bootstrap_module, DependencyModuleError


class DomainConfig(AppConfig):
    name = 'pizzaria.modules.domain'
    label = 'domain'
    verbose_name = 'Pizzaria - Módulo de Domínio'

    dependecies = ('pizzaria.modules.core',)

    @bootstrap_module
    def ready(self):
        for dependecy in self.dependecies:
            if not apps.is_installed:
                raise DependencyModuleError(self.name, dependecy)
        return
