import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyThread(QThread):
    msg = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.name = None
    def set_name(self,val):
        self.name = val
    def set_value(self,val):
        self.val = int(val)
        self.start()
    def run(self):
        print('线程开始执行',self.val)
        while self.val > 0 and self.name:
            self.msg.emit(self.val)
            self.val -= 1

class MyTest(QWidget):
    def __init__(self):
        super().__init__()
        self.thread = MyThread()
        self.thread.set_name('my')
        self.thread.msg.connect(self.text)
        self.thread.set_value(10)
        

    def text(self,val):
        print('截获到信号，值为：',val)

app = QApplication(sys.argv)
m = MyTest()
m.show()
sys.exit(app.exec_())

    