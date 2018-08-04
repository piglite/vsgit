#test QApplication.processEvents
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from time import sleep

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('processEvent Demo')
        self.resize(640,480)
        layout = QGridLayout()
        self.list = QListWidget()
        layout.addWidget(self.list,0,0,1,2)
        self.btn = QPushButton('start')
        layout.addWidget(self.btn,1,1)
        self.setLayout(layout)
        self.btn.clicked.connect(self.start_btn)
    
    def start_btn(self):
        for x in range(200):
            item = 'Num %d'%x
            self.list.addItem(item)
            QApplication.processEvents()
            sleep(1)

app = QApplication(sys.argv)
m = MyWindow()
m.show()
sys.exit(app.exec_())
