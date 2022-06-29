from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

cliente_api = Blueprint("cliente_api", __name__)


class clientesupermercado(BaseModel):
    __tablename__ = "cliente_supermercado"

    id = db.Column(db.Integer , primary_key=True)

    cliente = db.Column(db.Integer , db.ForeignKey("cliente.id"))
    supermercado = db.Column(db.Integer , db.ForeignKey("supermercado.id"))
class cliente(BaseModel):

    __tablename__ = "cliente"

    id = db.Column(db.Integer , primary_key=True)
    nome = db.Column(db.String(100))
    cpf= db.Column(db.String(11))
    ganero= db.Column(db.String(16))
    idade = db.Column(db.Integer)
    pedidos = db.relationship("entrega", backref="cliente")
    supermercados = db.relationship("supermercado", secondary = "cliente_supermercado", backref="clientes")
    suporte = db.relationship("suporte", backref="cliente")

    


