import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)
        layout.addWidget(QLabel('选择样式'))
        self.combo = QComboBox()
        layout.addWidget(self.combo)
        self.combo.addItems(QStyleFactory.keys())
        self.combo.activated[str].connect(self.handler)
    def handler(self,val):
        print('选择的样式是：',val)
        QApplication.setStyle(val)
    
app = QApplication(sys.argv)
w = MyWindow()
w.show()
app.exec_()
    