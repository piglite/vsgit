import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DateDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('dialog demo')
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.datetime = QDateTimeEdit(self)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.datetime)

        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,Qt.Horizontal,self)
        btns.accepted.connect(self.accept)
        btns.rejected.connect(self.reject)
        layout.addWidget(btns)
    
    def date_time(self):
        return self.datetime.dateTime()

    @staticmethod
    def getDateTime():
        dialog = DateDialog()
        result = dialog.exec_()
        d = dialog.date_time()
        return d.date(),d.time(),result == QDialog.Accepted
    
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400,300)
        self.setWindowTitle('MyWindow')
        self .setupUI()
    def setupUI(self):
        self.le = QLabel('xxx')
        self.btn1 = QPushButton('弹框1')
        self.btn2 = QPushButton('弹框2')
        self.btn1.clicked.connect(self.btn1_clk)
        self.btn2.clicked.connect(self.btn2_clk)
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.le)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)

    def btn1_clk(self):
        d = DateDialog()
        d.exec_()
        d2 = d.date_time()
        self.le.setText(d2.date().toString())
        d.destroy()

    def btn2_clk(self):
        date,time,result = DateDialog.getDateTime()
        self.le.setText(date.toString())

app = QApplication(sys.argv)
w = MyWindow()
w.show()
app.exec_()
        