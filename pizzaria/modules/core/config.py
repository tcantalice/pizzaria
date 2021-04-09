from django.apps import AppConfig

from pizzaria.bootstrap import handler_module_ready as init


class ModuleConfig(AppConfig):
    def __init__(self, app_name, app_module):
        super().__init__(app_name, app_module)
        self.label = self.__class__.module_label()

    @staticmethod
    def module_label():
        error_msg = f"Método 'module_label' não implementado para a classe '{__class__.__name__}'"
        raise NotImplementedError(error_msg)

    @classmethod
    def model_label(cls, model_name):
        return f'{cls.module_label()}.{model_name}'

class CoreConfig(ModuleConfig):
    name = 'pizzaria.modules.core'
    verbose_name = 'Pizzaria - Módulo Core'

    @init
    def ready(self):
        pass

    @staticmethod
    def module_label():
        return 'core'
