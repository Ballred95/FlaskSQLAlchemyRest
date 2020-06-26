from flask import Flask, Request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#init app
app = Flask(__name__)

#run server
if __name__ == '__main__':
    app.run(debug=True)