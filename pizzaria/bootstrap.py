"""
Contém funções úteis para o preparo dos módulos durante a inicialização
"""

from functools import wraps

import logging
from django.apps import registry

logger = logging.getLogger('bootstrap')

def __default_log(level, message, *args, **kwargs):
    '''Registra a mensagem no log padrão da aplicação'''
    logger.log(level, message, *args, **kwargs)


def __info_initialize_module(module_name):
    '''Log de informação da inicialização de carregamento do módulo'''
    message = "Iniciado carregamento do módulo '%s'"
    __default_log(logging.INFO, message, module_name)


def __info_finalize_module(module_name):
    '''Log de informação do encerramento de carregamento do módulo'''
    message = "Carregamento do módulo '%s' concluído com sucesso"
    __default_log(logging.INFO, message, module_name)


def __error_module(error):
    '''Log de erro durante o carregamento do módulo'''
    message = str(error)
    __default_log(logging.ERROR, message)


def bootstrap_module(ready):
    @wraps(ready)
    def wrapper(instance):
        module_name = instance.name

        __info_initialize_module(module_name)
        try:
            ready(instance)
        except Exception as e:
            __error_module(e)
        else:
            __info_finalize_module(module_name)

    return wrapper


def bootstrap_dependency_resolve(ready):
    @wraps(ready)
    def wrapper(instance):
        module_name = instance.name
        dependencies = instance.dependencies

        for dependency in dependencies:
            if not registry.apps.is_installed(dependency):
                raise DependencyModuleError(
                    dependent_module=module_name, dependency_module=dependency
                )
    return wrapper


class BootstrapModuleError(Exception):
    def __init__(self, message, *args) -> None:
        self.message = message
        super().__init__(*args)

    def __str__(self) -> str:
        class_name = self.__class__.__name__
        return '{}: {}'.format(class_name, self.message)


class DependencyModuleError(BootstrapModuleError):
    message_format = (
        "O módulo '{dependent}' requer o módulo '{dependency}' instalado"
    )

    def __init__(self, dependent_module, dependency_module, *args):
        super().__init__(
            self.message_format.format(
                dependent=dependent_module, dependency=dependency_module
            ),
            *args,
        )
