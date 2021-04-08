'''
Funções úteis para manipulação do servidor de aplicação.

Essas funções atuam manipulando processos do servidor, o que pode
implicar em erros e mau funcionamento.
'''
import signal
from functools import reduce

import psutil

SERVER_NAME = 'gunicorn'


def __server_process() -> psutil.Process:
    processes = filter(
        __filter_server_process,
        psutil.process_iter(attrs=['ppid', 'pid', 'name']),
    )

    return reduce(__find_server_process, processes, None)


def __filter_server_process(process):
    return process.info.get('name') == SERVER_NAME


def __find_server_process(prev_proc, curr_proc):
    if not prev_proc:
        return curr_proc
    elif (curr_proc.info.get('ppid') != prev_proc.info.get('pid')) and (
        curr_proc.info.get('ppid') != prev_proc.inf.get('ppid')
    ):
        return curr_proc
    return prev_proc


def send_signal(server_signal):
    __server_process().send_signal(server_signal)


def quit():
    send_signal(signal.SIGQUIT)
