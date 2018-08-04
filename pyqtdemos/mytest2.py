import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()
    
    def setupUI(self):
        self.setWindowTitle('Thread Demo')
        self.setGeometry(100,100,100+640,100+480)
        layout = QGridLayout()
        self.list = QListWidget()
        self.btn = QPushButton('Start')
        self.btn2 = QPushButton('Stop')
        self.btn2.setEnabled(False)
        layout.addWidget(self.list,0,0,1,2)
        layout.addWidget(self.btn,1,0)
        layout.addWidget(self.btn2,1,1)
       
        self.btn.clicked.connect(self.btn_start)
        self.btn2.clicked.connect(self.btn_stop)
        self.setLayout(layout)
        self.show()


    def btn_start(self):
        self.btn.setEnabled(False)
        self.btn2.setEnabled(True)
        self.thread = MyWorker()
        self.thread.sinout.connect(self.refresh_list)
        self.thread.start()
    def btn_stop(self):
        self.btn2.setEnabled(False)
        self.btn.setEnabled(True)
        self.thread.working = False
    
    def refresh_list(self,msg):
        self.list.addItem(msg)


class MyWorker(QThread):
    sinout = pyqtSignal(str)
    count = 0
    def __init__(self):
        super().__init__()
        self.working = True

    def __del__(self):
        print('__del__方法被调用了！')
        self.working = False
        self.wait()
    
    def run(self):
        while self.working:
            msg = '数字%d' % self.count
            self.count += 1
            self.sinout.emit(msg)
            self.sleep(1) #休眠的单位是：秒
    
app = QApplication(sys.argv)
win = MainWindow()
sys.exit(app.exec_())

