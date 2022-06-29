
from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

cliente_api = Blueprint("cliente_api", __name__)

class cliente(BaseModel):

    __tablename__ = "cliente"

    id = db.column(db.Integer , Primary_Key= True)
    nome = db.column(db.String(100))
    cpf= db.column(db.String(11))
    idade = db.column(db.Integer)
    entrega = db.relationship("entrega", backref="cliente")
    supermercado = db.column(db.Integer)
    suporte = db.relationship("suporte", backref="cliente")

    


