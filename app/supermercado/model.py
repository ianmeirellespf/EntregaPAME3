from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

supermercado_api = Blueprint("supermercado_api", __name__)

class supermercado(BaseModel):
    __tablename__ = "supermercado"
    
    id = db.Column(db.Integer , primary_key=True)
    unidade = db.Column(db.String(50))
    endereço= db.Column(db.String(100))
    receita = db.Column(db.Float)
    lucro = db.Column(db.Float)
    entregadores = db.relationship("entregador", backref="supermercado")