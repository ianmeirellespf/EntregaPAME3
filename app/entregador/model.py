from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

entregador_api = Blueprint("entregador_api", __name__)

class entregador(BaseModel):
    __tablename__ = "entregador"
    
    id = db.Column(db.Integer , primary_key=True)
    nome = db.column(db.String(100))
    cpf= db.column(db.String(11))
    genero= db.column(db.String(16))
    idade = db.column(db.Integer)
    entregas = db.relationship("entrega", backref="entregador")
    supermercado = db.column(db.Integer, db.ForeignKey("supermercado.id"))
    