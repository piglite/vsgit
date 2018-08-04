import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()
    
    def setupUI(self):
        self.setWindowTitle('Thread Demo')
        self.list = QListWidget()
        self.btn = QPushButton('Start')
        layout = QGridLayout()
        layout.addWidget(self.list,0,0,1,2)
        layout.addWidget(self.btn,1,1)
        self.setLayout(layout)
        self.btn.clicked.connect(self.startbtn)
        self.thread = Thread()
        self.thread.sinOut.connect(self.additem)

    def startbtn(self):
        self.btn.setEnabled(False)
        self.thread.start()
    
    def additem(self,file):
        self.list.addItem(file)

class Thread(QThread):
    sinOut = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.islive = True
        self.num = 0
        
        
    def __del__(self):
        self.islive = False
        self.wait()

    def run(self):
        while self.islive:
            msg = 'File index {}'.format(self.num)
            self.num += 1
            self.sinOut.emit(msg)
            self.sleep(2)

if __name__=='__main__':
    app = QApplication(sys.argv)
    demo = MyWindow()
    demo.show()
    sys.exit(app.exec_())




    
    


