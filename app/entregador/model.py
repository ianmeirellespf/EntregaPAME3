from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

entregador_api = Blueprint("entregador_api", __name__)

class entregador(BaseModel):
    __tablename__ = "entregador"
    
    id = db.Column(db.Integer , primary_key=True)
    nome = db.Column(db.String(100))
    cpf= db.Column(db.String(11))
    genero= db.Column(db.String(16))
    idade = db.Column(db.Integer)
    entregas = db.relationship("entrega", backref="entregador")
    supermercado = db.Column(db.Integer, db.ForeignKey("supermercado.id"))
    