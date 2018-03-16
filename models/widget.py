
from marshmallow import Schema, fields, pre_load, validate
from database import db
from database import ma

class Widget(db.Model):
    __tablename__ = 'widgets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512), nullable=False)
    price = db.Column(db.Numeric, nullable=False)

    def __init__(self, name, price):
        self.name = name
        self.price = price

class WidgetSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    price = fields.Number(required=True)