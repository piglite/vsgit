import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()
    
    def setupUI(self):
        self.setWindowTitle('signal demo')
        layout = QVBoxLayout()
        btn = QPushButton('Click',self)
        layout.addWidget(btn)
        self.setLayout(layout)
        btn.setObjectName('mybtn')
        QMetaObject.connectSlotsByName(self)
    
    @pyqtSlot()
    def on_mybtn_clicked(self):
        print('按钮被点击了')
    
app = QApplication(sys.argv)
w = MyWidget()
w.show()
sys.exit(app.exec_())
    
