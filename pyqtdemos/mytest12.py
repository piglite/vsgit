import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from time import sleep

class MyThread(QThread):
    msg = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        
    def run(self):
        while True:
            date = QDateTime.currentDateTime()
            s = date.toString('yyyy-MM-dd HH:mm:ss')
            print('线程中的时间',s)
            self.msg.emit(s)
            sleep(1)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Time Demo')
        self.resize(400,150)
        layout = QHBoxLayout()
        self.lb = QLineEdit()
        self.lb.resize(400,150)
        layout.addWidget(self.lb)
        self.setLayout(layout)
        self.thread = MyThread()
        self.thread.msg.connect(self.handler)
        self.thread.start()
    def handler(self,s):
        self.lb.setText(s)

app = QApplication(sys.argv)
w = MyWindow()
w.show()
sys.exit(app.exec_())
        

