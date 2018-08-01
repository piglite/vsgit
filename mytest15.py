import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('绘画Demo')
        self.pix = QPixmap(400,400)
        self.pix.fill(Qt.white)
        self.startPoint = QPoint()
        self.endPoint = QPoint()
        self.resize(500,500)
        
    
    def paintEvent(self,event):
        print('paintEvent方法调用')
        painter = QPainter(self.pix)
        painter.setPen(QColor(255,0,0))
        print(self.startPoint,self.endPoint)
        painter.drawLine(self.startPoint,self.endPoint)
        self.startPoint = self.endPoint
        p = QPainter(self)
        p.drawPixmap(0,0,self.pix)
    
    def mousePressEvent(self,event):
        print('mousePress方法执行')
        if event.button()==Qt.LeftButton:
            self.startPoint = event.pos()
            self.endPoint = self.startPoint

    def mouseMoveEvent(self,event):
        print('mouseMove方法执行')
        if event.buttons() and Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()
    def mouseReleaseEvent(self,event):
        print('mouseRelease方法执行')
        if event.buttons()==Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()
    
app = QApplication(sys.argv)
w = MyWindow()
w.show()
sys.exit(app.exec_())



        
