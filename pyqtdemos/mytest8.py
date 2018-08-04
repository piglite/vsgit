#QWebView calling JavaScript
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebChannel import *

class MyObj(QWidget):
    def __init__(self):
        super().__init__()
    
    def getstrvalue(self):
        return '100'
    def setstrvalue(self,val):
        print('来自页面的参数：',val)
        QMessageBox.information(self,'info','获得的页面参数:%s'%val)
    
    strval = pyqtProperty(str,fget=getstrvalue,fset=setstrvalue)


app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle('数据交互')

layout = QVBoxLayout()
win.setLayout(layout)

view = QWebEngineView()
url = 'http://127.0.0.1:8020/pyqttest/index.html'
view.load(QUrl(url))

channel = QWebChannel()
myobj  =  MyObj()
channel.registerObject('bridge',myobj)
view.page().setWebChannel(channel)
layout.addWidget(view)

win.show()
sys.exit(app.exec_())
