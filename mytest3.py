#test QThread
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

sec = 0

def set_time():
    global sec
    sec += 1
    lcd.display(sec)

def work():
    timer.start(1000)
    my_thread.start()
    my_thread.sin_out.connect(stop_time)

def stop_time():
    timer.stop()
    print('运行结束：',lcd.value())
    global sec
    sec = 0

class MyThread(QThread):
    sin_out = pyqtSignal()
    def __init__(self):
        super().__init__()
    def run(self):
        print('线程开始执行...')
        for x in range(200000000):
            pass
        print('线程结束执行...')
        self.sin_out.emit()

app = QApplication(sys.argv)
w = QWidget()
w.resize(300,240)

layout = QVBoxLayout(w)
lcd = QLCDNumber()
layout.addWidget(lcd)
btn = QPushButton('start')
btn.clicked.connect(work)
layout.addWidget(btn)
w.show()
my_thread = MyThread()
timer = QTimer()
timer.timeout.connect(set_time)
sys.exit(app.exec_())

