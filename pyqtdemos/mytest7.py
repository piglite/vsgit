#QWebView calling JavaScript
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle('Test Calling JS')

layout = QVBoxLayout()
win.setLayout(layout)

view = QWebEngineView()
html = '''
    <html>
        <head>
        <title>Demo PAge</title>
        <script>
            function my(){
                var fname = document.getElementById('fname').value;
                var lname = document.getElementById('lname').value;
                var full = fname +' '+lname;
                document.getElementById('fullname').value = full;
                document.getElementById('submit-btn').style.display = 'block';
                return full;
            }
        </script>
        </head>
        <body>
            <form>
                <input type='text' name='fname' id='fname'><br/>
                <input type='text' name='lname' id='lname'><br/>
                <input type='text' name='fullname' id='fullname'><br/>
                <input style='display:none;' type='submit' id='submit-btn'>
            </form>
        </body>
    </html>

'''
view.setHtml(html)

def complete_name():
    view.page().runJavaScript('my();',js_callback)

def js_callback(result):
    print('js代码的执行结果',result)

btn = QPushButton('set name')
layout.addWidget(view)
layout.addWidget(btn)
btn.clicked.connect(complete_name) 


win.show()
sys.exit(app.exec_())
