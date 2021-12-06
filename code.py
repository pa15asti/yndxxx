from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
import sys
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.Qt import QMainWindow
import random as r


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi('ui.ui', self)
        self.pushButton.clicked.connect(self.onClicked)
        self.flag = False

    def onClicked(self):
        self.flag = True
        self.update()


    def paintEvent(self, e):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawRectangles(qp)
            qp.end()

    def drawRectangles(self, qp):
        a = r.randint(10, 100)
        rndm = r.choice((1, 2, 3))
        if rndm == 1:
            qp.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
            qp.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            qp.drawEllipse(r.randint(10, 400), r.randint(10, 400), a, a)
        elif rndm == 2:
            qp.setPen(QPen(Qt.red, 8, Qt.SolidLine))
            qp.setBrush(QBrush(Qt.red, Qt.SolidPattern))
            qp.drawEllipse(r.randint(10, 400), r.randint(10, 400), a, a)
        else:
            qp.setPen(QPen(Qt.blue, 8, Qt.SolidLine))
            qp.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
            qp.drawEllipse(r.randint(10, 400), r.randint(10, 400), a, a)
            
            
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(448, 278)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(163, 20, 113, 32))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Жми"))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
