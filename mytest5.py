#test webEngineView
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self):
        self.setWindowTitle('WebEngineView Demo')
        self.resize(1024,768)
        self.browser = QWebEngineView()
        self.browser.load(QUrl('http://www.sohu.com'))
        self.setCentralWidget(self.browser)
        self.show()

app = QApplication(sys.argv)
w = MyWindow()
sys.exit(app.exec_())
