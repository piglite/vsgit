import requests
from bs4 import BeautifulSoup
import json
from time import sleep
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello flask!'

app.run()

