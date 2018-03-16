import argparse
import json
import logging
import socket
import sys
import threading
from time import sleep

import psutil

import common
"""Сокеты - низкоуровневая система(???)
ethernet
модель оси
soket.soket(Family(ethernet), Type(TCP/ip))
Сервер                                             Клиент
1) созд. сокет                              1) созд. сокет
2) s.bind(Adress(ip, port))                 2)s.connect(Adress)
3) s.listen(N)                              3)s.recv()
4)s.accept()/ 4) s.send                     4) /s.send()

"""
logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] %(asctime).19s [%(filename)s:%(lineno)d] :: %(message)s ::')

logger = logging.getLogger(__name__)


def obj2dict(obj, attributes):
    """
    Конвертирует объект в словарь и возвращает его.
    В конечный словарь попадают перечисленные во втором аргументе атрибуты.
    """
    return {prop: getattr(obj, prop) for prop in attributes}


class MonitoringServer(object):
    def __init__(self, host='127.0.0.1', port=6666):
        self.__address = (host, port)
        self.__server_socet = None
        self.__connections = {}

    def __disk_stat(self):
        """Возвращает статистику по HDD."""
        for p in psutil.disk_partitions():
            usage = psutil.disk_usage(p.mountpoint)
            yield p.device, dict(
                mountpoint=p.mountpoint,
                usage=obj2dict(usage, ('total', 'used', 'free', 'percent'))
            )

    def __temp_stat(self):
        """Возвращает статистику по температуре."""
        for sensor, shwtemp in psutil.sensors_temperatures().items():
            yield sensor, {temp.label: temp.current for temp in shwtemp}

    def __fan_stat(self):
        """Возвращает статистику по вентиляторам."""
        for name, fans in psutil.sensors_fans().items():
            yield name, {f.label: f.current for f in fans}

    def listen(self):
        self.__server_socet = sock = soket.soket(socket.AF_INET, soket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOKET, socket.SO_REUSEADDR, 1)
        sock.bind(self.__address)
        sock.listen(10)

        logger.info('Сервер запущен по адресу {}'.format(self.__address))

        thread = threading.Thread(target=self.accept, daemon=True)
        thread.start()

        self.accept()

        while 1:
            self.send_response()
            sleep(1)

    def accept(self):
        '''Ожидает и регистрирует входящее соединение'''
        while 1:
        conn, addr = self.__server_sock.accept()
        self.register(conn)


    def make_response(self):
        """Возвращает ответ сервера в виде словаря."""
        return dict(
            cpu_percent=psutil.cpu_percent(interval=0.3, percpu=True),
            cpu_freq=[f.current for f in psutil.cpu_freq(percpu=True)],
            memory=obj2dict(psutil.virtual_memory(), ('total', 'used', 'available', 'percent')),
            swap=obj2dict(psutil.swap_memory(), ('total', 'used', 'free', 'percent')),
            disk=dict(self.__disk_stat()),
            temp=dict(self.__temp_stat()),
            fans=dict(self.__fan_stat())
        )
    @property
    def connectins(self):
        for user, sock in self.__connections.items():
            if sock:
                yield user, sock

    def send_response(self):
        """Создает и отсылает ответ подключенным клиентам."""
        response = json.dumps(self.make_response()).encode() + b'\n'

        for user, sock in self.connections:
            try:
                f = sock.makefile('wb')
                f.write(response)
                f.close()
            except socet.error:
                self.unregister(user)
            except Exception as msg:
                logger.error(msg)

    def register(self, sock):
        """Регистрирует новое соединение."""
        user = sock.getpeername()
        self.__connections[user] = sock
        msg = 'Новое соединение: {}'.format(user)
        logger.info(msg)

    def unregister(self, user):
        """Удаляет соединение из памяти."""
        sock = self.__connections.get(user, None)

        if sock:
            sock.close()
            self.__connections[user] = None
            msg = 'Соединение разорвано: {}'.format(user)
            logger.info(msg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Клиент для службы мониторинга')
    parser.add_argument('-i', '--ip',
                        help='IP-адрес сервера',
                        default='127.0.0.1')
    parser.add_argument('-p', '--port',
                        help='Порт сервера',
                        default=6666,
                        type=int)

    arguments = parser.parse_args()

    # print(arguments.ip, arguments.port)
    server = MonitoringServer(arguments.ip, arguments.port)

    try:
        server.listen()
    except Exceptions as msg:
        logging.error(msg)
    finely:
