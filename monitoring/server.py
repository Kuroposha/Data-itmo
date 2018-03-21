# coding: utf-8
#
# Copyright 2018 Kirill Vercetti
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import json
import logging
import socket
import sys
import threading
from time import sleep

import psutil

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
        self.__server_socket = None
        self.__connections = []

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

    def __encode_response(self, response):
        """Кодирует ответ для дальнейшей отправки через сокет."""
        return json.dumps(response).encode() + b'\n'

    def __send(self, sock, response):
        """Записывает в указанный сокет предварительно закодированный ответ."""
        try:
            f = sock.makefile('wb')
            f.write(response)
            f.close()
        except socket.error:
            self.unregister(sock)
        except Exception as msg:
            logger.error(msg)

    def accept(self):
        """Ожидает и регистрирует входящее соединение."""
        while 1:
            conn, addr = self.__server_socket.accept()
            self.on_first_request(conn)
            self.register(conn)

    @property
    def connections(self):
        return self.__connections

    def listen(self):
        """Запускает сервер на прослушивание входящих соединений."""
        self.__server_socket = server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(self.__address)
        server_socket.listen(10)

        logger.info('Сервер запущен по адресу {}'.format(self.__address))

        thread = threading.Thread(target=self.accept, daemon=True)
        thread.start()

        while 1:
            self.send_response()
            sleep(1)

    def make_response(self):
        """Возвращает ответ сервера в виде словаря."""
        return dict(
            cpu_percent=psutil.cpu_percent(interval=0.3, percpu=True),
            cpu_freq=[f.current for f in psutil.cpu_freq(percpu=True)],
            memory=obj2dict(psutil.virtual_memory(), ('used', 'available', 'percent')),
            swap=obj2dict(psutil.swap_memory(), ('used', 'free', 'percent')),
            disk=dict(self.__disk_stat()),
            temp=dict(self.__temp_stat()),
            fans=dict(self.__fan_stat())
        )

    def get_system_info(self):
        """Возвращает информацию о системе."""
        cpu_freq = psutil.cpu_freq()
        return dict(cpu_count=psutil.cpu_count(),
                    cpu_freq_min=cpu_freq.min,
                    cpu_freq_max=cpu_freq.max,
                    memory_total=psutil.virtual_memory().total,
                    swap_total=psutil.swap_memory().total)

    def on_first_request(self, sock):
        """Выполняется при первом запросе клиента и отсылает информацию о машине."""
        response = self.__encode_response(self.get_system_info())
        self.__send(sock, response)

    def send_response(self):
        """Создает и отсылает ответ подключенным клиентам."""
        response = self.__encode_response(self.make_response())

        for sock in self.connections:
            self.__send(sock, response)

    def register(self, sock):
        """Регистрирует новое соединение."""
        user = sock.getpeername()
        self.__connections.append(sock)
        msg = 'Новое соединение: {}'.format(user)
        logger.info(msg)

    def unregister(self, sock):
        """Удаляет соединение из памяти."""
        sock.close()
        self.__connections.remove(sock)
        logger.info('Соединение разорвано')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Служба мониторинга')

    parser.add_argument('-i', '--ip', help='IP адрес сервера', default='127.0.0.1')
    parser.add_argument('-p', '--port', help='Порт сервера', default='6666', type=int)

    arguments = parser.parse_args()

    server = MonitoringServer(arguments.ip, arguments.port)

    try:
        server.listen()
    except Exception as msg:
        logger.error(msg)
    finally:
        sys.exit(0)
