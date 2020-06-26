from flask import Flask, Request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#init db
db = SQLAlchemy(app)
#init ma
ma = Marshmallow(app)

#Class/Model
class Product(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique = True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    #constructor
    def __init__(self, name, desription, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

#Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id' 'name' 'description', 'price', 'qty')

#init Schema
product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(many=True, strict=True)

#run server
if __name__ == '__main__':
    app.run(debug=True)