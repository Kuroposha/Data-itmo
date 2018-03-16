import argparse
import json
import logging
import socket
import common

class Client(object):
    def __init__(self, host, port):
        self.__address = (host, port)
        self.__client_socket = None

    def __connect(self):
        self.__client_socket = sock = socket.socket(socket.AF_INET,
                                                    socket.SOCK_STREAM)

        try:
            sock.connect(self.__address)
            msg = 'Установлено соединение с {}'.format(self.__address)
        except socket.error:
            logging.error('Сервер недоступен')

    def get_response(self):
        with self.__client_socket.makefile('rb') as f:
            while 1:
                response = f.readline()

                if not response:
                    break
                yield json.loads(response.decode())
                
    def run(self):
        print('Run')

    def check(self):
        print('Check')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cлужбы мониторинга')
    parser.add_argument('-i', '--ip',
                        help='IP-адрес сервера',
                        default='127.0.0.1')

    parser.add_argument('-p', '--port',
                        help='Порт сервера',
                        default=6666,
                        type=int)
    parser.set_defaults(callback=lambda cli: parser.print_help())

    subparsers = parser.add_subparsers()

    parser_check = subparsers.add_parser('check',
                                         help='Выполнить проверку',
                                         description='Получить текущее состояние')

    # parser_check.add_argument('-d', '--demo',
                            #   help='For demo')
    parser_check.set_defaults(callback=lambda cli: cli.check())

    run_parser = subparsers.add_parser('run',
                                       help='Запустить мониторинг',
                                       description='Запустить мониторинг в режиме рв')
    run_parser.set_defaults(callback=lambda cli: cli.run())
    arguments = vars(parser.parse_args())

    client = Client(arguments.pop('ip', None), arguments.pop('port'))

    arguments.pop('callback')(client, **arguments)
