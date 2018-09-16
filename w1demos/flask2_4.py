from flask import Flask
from flask import request,current_app,render_template,url_for
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    print(app.url_map )
    #return '<h1>hello flask</h1>',404,{'myhead':'test'}
    return render_template('index.html         ')
    
    
@app.route('/user/<name>')
def say(name):
    print(request.headers.get('User-Agent'))
    return '<h1>hello %s</h1>' % name

@app.errorhandler(404)
def page_not_found(err):
    print(url_for('say',name='ABC',_external=True))
    print(url_for('index',name='ABC',_external=True))
    return render_template('my404.html'),404

if __name__=='__main__':
    app.run(debug=True,port=9898)