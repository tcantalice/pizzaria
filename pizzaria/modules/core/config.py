from django.apps import AppConfig

from pizzaria.bootstrap import bootstrap_module

class CoreConfig(AppConfig):
    name = 'pizzaria.modules.core'
    label = 'core'
    verbose_name = 'Pizzaria - Módulo Core'

    @bootstrap_module
    def ready(self):
        return