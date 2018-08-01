#test load local html
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from os.path import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('WebView Demo')
        self.setGeometry(5,30,1024,768)
        self.webview = QWebEngineView()
        url = join(dirname(__file__),'html\index.html')
        print(url)
        self.webview.load(QUrl('D:/VSProjects/index.html'))
        self.setCentralWidget(self.webview)
        self.show()
app = QApplication(sys.argv)
w = MyWindow()
sys.exit(app.exec_())

