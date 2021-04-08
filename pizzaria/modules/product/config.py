from pizzaria.modules.core.config import ModuleConfig
from pizzaria.bootstrap import (
    handler_module_ready as init,
    check_module_dependencies as check_dependencies
)


class ProductConfig(ModuleConfig):
    name = 'pizzaria.modules.product'
    verbose_name = 'Pizzaria - Módulo de Produtos'

    dependencies = ('pizzaria.modules.core',)

    @init
    def ready(self):
        check_dependencies(self.name, self.dependencies)

    @staticmethod
    def module_label():
        return 'product'
