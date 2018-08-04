#播放gif
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class LoadingGIF(QWidget):
    def __init__(self):
        super().__init__()
        self.lb = QLabel('',self)
        self.setFixedSize(128,128)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.movie = QMovie('images/ch8/loading.gif')
        self.lb.setMovie(self.movie)
        self.movie.start()

app = QApplication(sys.argv)
m = LoadingGIF()
m.show()
sys.exit(app.exec())

