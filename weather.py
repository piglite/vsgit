import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import requests



class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('天气')
        self.resize(800,600)
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(QLabel('查询城市天气'))
        w = QWidget()
        hlayout = QHBoxLayout(self)
       
        hlayout.addWidget(QLabel('选择城市：'))
        self.cb = QComboBox()
        self.cb.addItem('北京')
        self.cb.addItem('上海')
        self.cb.addItem('天津')
       
        hlayout.addWidget(self.cb,Qt.AlignLeft)
        w.setLayout(hlayout)
        layout.addWidget(w)
        self.textedit = QTextEdit()
        layout.addWidget(self.textedit)
        w = QWidget()
        hlayout = QHBoxLayout(self)
        self.query = QPushButton('查询')
        self.clear = QPushButton('清空')
        self.query.clicked.connect(self.get_weather)
        self.clear.clicked.connect(self.clear_text)
        hlayout.addWidget(self.query)
        hlayout.addWidget(self.clear)
        w.setLayout(hlayout)
        layout.addWidget(w)
    def clear_text(self):
        self.textedit.setText('')
    def get_weather(self,u=None):
        if not u:
            cityname = self.cb.currentText()
            print(cityname)
            citycode = self.get_citycode(cityname)
            u = 'http://www.weather.com.cn/data/sk/'+citycode+'.html'
        req = requests.get(u)
        req.encoding='utf-8'
        result = req.json()
        info = result['weatherinfo']
        msg1 = '城市：' + info.get('city',None)+'\n'
        msg2 = '温度：' + info.get('temp',None)+'\n'
        msg3 = '风向：' + info.get('WD',None)+'\n'
        msg4 = '风力：' + info.get('WS',None)+'\n'
        msg5 = '湿度：' + info.get('SD',None)+'\n'
        self.textedit.setText('%s%s%s%s%s'%(msg1,msg2,msg3,msg4,msg5))

    def get_citycode(self,cityname):
        if cityname=='北京':
            citycode =  '101010100'
        elif cityname=='天津':
            citycode = '101030100'
        else: 
            citycode =  '101020100'
        return citycode

app = QApplication(sys.argv)
w = MyWindow()
w.show()
sys.exit(app.exec())
