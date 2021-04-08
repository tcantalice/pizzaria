from django.apps import AppConfig

from pizzaria.bootstrap import handler_module_ready as init

class CoreConfig(AppConfig):
    name = 'pizzaria.modules.core'
    verbose_name = 'Pizzaria - Módulo Core'

    def __init__(self, app_name, app_module):
        super().__init__(app_name, app_module)
        self.label = self.__class__.module_label()

    @init
    def ready(self):
        return

    @staticmethod
    def module_label():
        return 'core'
