from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap
from flask import Flask,render_template

class NameForm(Form):
    name = StringField('Your Name...',validators=[Required()])
    submit_btn = SubmitField('submit')

app = Flask(__name__)
app.config['SECRET_KEY']='time to say hello'
Bootstrap(app)

@app.route('/',methods=['GET','POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index2.html',name=name,form=form)

app.run(debug=True)