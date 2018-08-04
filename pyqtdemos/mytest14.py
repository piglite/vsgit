import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:blue;')
        desk = QApplication.desktop()
        rect = desk.availableGeometry()
        self.setGeometry(rect)
        self.show()
app = QApplication(sys.argv)
w = MyWindow()
app.exec_()
        