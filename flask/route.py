from app import *
from flask import jsonify, request
from models import * 

def get_single(model,schema,id):
    aValue = model.query.get(id)
    return schema.jsonify(aValue)

def get_all(model,schema):
    aValue = model.query.all()
    result = schema.dump(aValue)
    return jsonify(result)

def create(model,schema):
    date = request.json['date']
    valeur = request.json['valeur']
    new_value = model(date, valeur)
    db.session.add(new_value)
    db.session.commit()
    return schema.jsonify(new_value)

def update(model,schema, id):
    value = model.query.get(id)
    date = request.json['date']
    valeur = request.json['valeur']
    value.date = date
    value.valeur = valeur
    db.session.commit()
    return schema.jsonify(value)

def delete(model,schema, id):
    value = model.query.get(id)
    db.session.delete(value)
    db.session.commit()
    return schema.jsonify(value)