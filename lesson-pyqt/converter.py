import sys

from PyQt5.QtCore import QObject, Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QDoubleSpinBox, QPushButton,
    QVBoxLayout
)


class Converter(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUi()
        self.initLayouts()
        self.initSignals()


    def initUi(self):
        self.setWindowTitle('Конвертер валют')

        self.srcLabel = QLabel('Сумма в рублях', self)
        #Не забывайте про родителя! обязательно его передавать
        self.resultLabel = QLabel('Сумма в долларах', self)

        self.srcAmount = QDoubleSpinBox(self)
        self.srcAmount.setMaximum(999999999)

        self.resultAmount = QDoubleSpinBox(self)
        self.resultAmount.setMaximum(999999999)
        #self.resultAmount.setReadOnly(True)

        self.convertBtn = QPushButton('Перевести', self)
        self.convertBtn.setDisabled(True)

        self.clearBtn = QPushButton('Сбросить', self)


    def initSignals(self):
        self.convertBtn.clicked.connect(self.onClickConvertBtn)
        self.clearBtn.clicked.connect(self.onClickClearBtn)
        self.srcAmount.valueChanged.connect(self.setButtonAvailability)
        self.resultAmount.valueChanged.connect(self.setButtonAvailability)


    def initLayouts(self):
        w = QWidget(self)
        # self.mainLayout = QVBoxLayout()

        self.mainLayout = QVBoxLayout(w)
        self.mainLayout.addWidget(self.srcLabel)
        self.mainLayout.addWidget(self.srcAmount)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addWidget(self.resultAmount)
        self.mainLayout.addWidget(self.convertBtn)
        self.mainLayout.addWidget(self.clearBtn)

        self.setCentralWidget(w)


    def onClickConvertBtn(self):
        src_value = self.srcAmount.value()
        res_value = self.resultAmount.value()

        if src_value:
            self.resultAmount.setValue(src_value / 30)
        elif res_value:
            self.srcAmount.setValue(res_value * 30)
            #setValue можно исп как слот

    def onClickClearBtn(self):
        self.resultAmount.setValue(0)
        self.srcAmount.setValue(0)

    def setButtonAvailability(self):
        src_value = self.srcAmount.value()
        res_value = self.resultAmount.value()
        # check = src_value and res_value

        if src_value and res_value or not src_value and not res_value:
            self.convertBtn.setDisabled(True)
        else:
            self.convertBtn.setDisabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    c = Converter()
    c.show()

    sys.exit(app.exec_())
