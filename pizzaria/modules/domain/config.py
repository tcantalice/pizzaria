from django.apps import registry

from pizzaria.modules.core.config import ModuleConfig
from pizzaria.bootstrap import (
    handler_module_ready as init,
    check_module_dependencies as check_dependencies
)


class DomainConfig(ModuleConfig):
    name = 'pizzaria.modules.domain'
    verbose_name = 'Pizzaria - Módulo de Domínio'

    dependencies = ('pizzaria.modules.core',)

    @init
    def ready(self):
        check_dependencies(self.name, self.dependencies, registry)

    @staticmethod
    def module_label():
        return 'domain'

