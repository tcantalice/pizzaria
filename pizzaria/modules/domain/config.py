from django.apps import AppConfig, registry

from pizzaria.bootstrap import (
    handler_module_ready as init,
    check_module_dependencies as check_dependencies,
)


class DomainConfig(AppConfig):
    name = 'pizzaria.modules.domain'
    label = 'domain'
    verbose_name = 'Pizzaria - Módulo de Domínio'

    dependencies = ('pizzaria.modules.core',)

    @init
    def ready(self):
        check_dependencies(self.name, self.dependencies, registry)
