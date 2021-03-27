"""
Contém funções úteis para o preparo dos módulos durante a inicialização
"""

from functools import wraps

from pendulum import now

CONSOLE_BOOTSTRAP_INFO = '[{time}] [BOOTSTRAP] [INFO]'
CONSOLE_BOOTSTRAP_ERROR = '[{time}] [BOOTSTRAP] [ERROR]'
CONSOLE_BOOTSTRAP_ALERT = '[{time}] [BOOTSTRAP] [ALERT]'

def __console_log(message_format, **kwargs):
    print(message_format.format(**kwargs))


def bootstrap_module(ready):
    def __bootstrap_module(ready):
        @wraps(ready)
        def wrapper(self, *args):
            START_FORMAT = CONSOLE_BOOTSTRAP_INFO + " Iniciado carregamento do módulo - '{name}'"
            ERROR_FORMAT = CONSOLE_BOOTSTRAP_ERROR + ' {error}'
            END_FORMAT = CONSOLE_BOOTSTRAP_INFO + " Carregamento do módulo '{name}' concluído com sucesso"

            module_name = self.name

            __console_log(
                START_FORMAT,
                time=now().to_datetime_string(),
                name=module_name
            )
            try:
                ready(self)
            except Exception as e:
                __console_log(
                    ERROR_FORMAT,
                    time=now().to_datetime_string(),
                    error=e
                )
            else:
                __console_log(
                    END_FORMAT,
                    time=now().to_datetime_string(),
                    name=module_name
                )

        return wrapper

    return __bootstrap_module(ready)
