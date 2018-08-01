import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MySignal(QObject):
    sin1 = pyqtSignal()
    sin2 = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.sin1.connect(self.handler1)
        self.sin1.connect(self.handler2)
        self.sin2.connect(self.handler3)
        self.sin2.connect(self.sin1)
        self.sin1.emit()
        self.sin2.emit(100)

    def handler1(self):
        print('handler1截获到信号')
    
    def handler2(self):
        print('handler2截获到信号')

    def handler3(self,value):
        print('handler3截获到信号啦啦啦',value)
    
s = MySignal()
    
