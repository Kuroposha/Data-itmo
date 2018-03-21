from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5.uic import loadUi
from core.ResponseGetter import ResponseGetter

class LoginWidget(QWidget):
    logged = pyqtSignal(str, int)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._initUi()
        self._initSignals()


    def _initUi(self):
        loadUi('gui/ui/loging_widget.ui', self)
        self.flushMessage()


    def _initSignals(self):
        self.connectBtn.clicked.connect(self.onLofin)


    def showMessage(self, message):
        # self.flashMessage.clear()
        self.flashMessage.setText(message)
        self.flashMessage.show()


    def flushMessage(self):
        self.flashMessage.clear()
        self.flashMessage.hide()

    def onLogin(self):
        host = self.hostEdit.text()
        port = self.portEdit.value()

        if host and port:
            self.logged.emit(host, port)
        else:
            self.showMessage('Введите адрес сервера')

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._getter = ResponseGetter(self)
        self._initUi()
        self._initSignals()


    def _initUi(self):
        loadUi('gui/ui/loging_widget.ui', self)
        self.resize(800, 600)
        #showFullScreen

        self.loginWidget = loginWidget(self)

        self.stackedWidget.addWidget(self.loginWidget)

        self.showLoginWidget()


    def _initSignals(self):
        self.loginWidget.logget.connect(self._getter.connect)

        
    def showLoginWidget(self):
        self.stackedWidget.setCurrentWiget(self.loginWidget)
