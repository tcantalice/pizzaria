from django.apps import AppConfig

from pizzaria.bootstrap import handler_module_ready as init

class CoreConfig(AppConfig):
    name = 'pizzaria.modules.core'
    label = 'core'
    verbose_name = 'Pizzaria - Módulo Core'

    @init
    def ready(self):
        return
