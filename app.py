from flask import Flask, Request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#init app
app = Flask(__name__)

#create route 
@app.route('/', methods = ['GET'])
def get():
    return jsonify({'msg': 'hello world'})

#run server
if __name__ == '__main__':
    app.run(debug=True)