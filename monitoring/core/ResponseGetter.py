import json
import socket
import threading
from time import sleep

from PyQt5.QtCore import QObject, pyqtSignal

class ResponseGetter(QObject):
    started = pyqtSignal(dict)
    disconnected = pyqtSignal()
    readyCPULoad = pyqtSignal(list)
    readyCPUFreq = pyqtSignal(list)
    readyMemory = pyqtSignal(int, float, int)
    readySwap = pyqtSignal(int, float, int)


    def _wait(self, sock):
        onStart = True
        with socket.makefile('rb') as f:
            while 1:
                data = f.readline()

                if not data:
                    self.disconnected.emit()
                    break

                response = json.loads(data.decode())

                if onStart:
                    self. started.emit(response)
                    onStart = False
                else:
                    self.readyCPULoad.emit(response.get('cpu_percent'))
                    self.readyCPUFreq.emit(response.get('cpu_freq'))

                    memory = response.get('memory')
                    self.readyMemory.emit(memory.get('used'),
                                          memory.get('percent'),
                                          memory.get('availble'))
                    swap = response.get('swap')
                    self.readySwap.emit(swap.get('used'),
                                        swap.get('percent'),
                                        swap.get('free'))

                sleep(1)

    def connect(self, host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                socket.connect((host, port))
                thread = threading.Thread(target=self._wait,
                                          args=(sock,),
                                          daemon=True)
                thread.start()
            except ConnectionRefusedError:
                self.disconnected.emit()
