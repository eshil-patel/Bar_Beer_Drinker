from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request
import json

from BarBeerDrinker import database
app = Flask(__name__)

app= Flask(__name__)

@app.route('/api/bar',methods['GET'])
def get_bars():
    jsonify(database.get_bars())
@app.route('/')
def hello_world():
    return 'Hello world!'
