import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()
    
    def setupUI(self):
        self.setWindowTitle('复利计算')
        self.setWindowIcon(QIcon('images/ch8/cartoon1.ico'))
        layout = QFormLayout()
        self.sp_cash = QDoubleSpinBox()
        self.sp_cash.setRange(1,100000000)
        self.sp_cash.setValue(10000)
        self.sp_cash.setPrefix('RMB')
        self.sp_cash.setSuffix('元')
        self.sp_cash.valueChanged.connect(self.get_amount)
        layout.addRow('启动资金',self.sp_cash)
        self.sp_rate = QDoubleSpinBox()
        self.sp_rate.setRange(1,100)
        self.sp_rate.setValue(5)
        self.sp_rate.setSuffix('%')
        self.sp_rate.valueChanged.connect(self.get_amount)
        layout.addRow('年利率',self.sp_rate)
        self.cb_year = QComboBox()
        self.cb_year.addItem('1 year')
        self.cb_year.addItems(['%d years'%x for x in range(2,6)])
        self.cb_year.currentTextChanged.connect(self.get_amount)
        layout.addRow('年限',self.cb_year)
        self.lb_amount = QLabel('xxxx')
        layout.addRow('总计',self.lb_amount)
        self.get_amount()
        self.setLayout(layout)
    
    def get_amount(self):
        cash = self.sp_cash.value()
        rate = self.sp_rate.value()
        year = int(self.cb_year.currentText()[0])
        amount =  cash*((1+rate/100)**year)
        self.lb_amount.setText('RMB %.2f'%amount)

app = QApplication(sys.argv)
w = MyWindow()
w.show()
sys.exit(app.exec())



