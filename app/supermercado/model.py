from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

supermercado_api = Blueprint("supermercado_api", __name__)

class supermercado(BaseModel):
    __tablename__ = "supermercado"
    
    id = db.Column(db.Integer , primary_key=True)
    unidade = db.column(db.String(50))
    endereço= db.column(db.String(100))
    receita = db.column(db.Float)
    lucro = db.column(db.Float)
    entregadores = db.relationship("entregador", backref="supermercado")