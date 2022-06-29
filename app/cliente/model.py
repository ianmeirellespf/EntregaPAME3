from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

cliente_api = Blueprint("cliente_api", __name__)


class clientesupermercado(BaseModel):
    __tablename__ = "cliente_supermercado"

    id = db.Column(db.Integer , primary_key=True)

    cliente = db.column(db.Integer , db.ForeignKey("cliente.id"))
    supermercado = db.column(db.Integer , db.ForeignKey("supermercado.id"))
class cliente(BaseModel):

    __tablename__ = "cliente"

    id = db.Column(db.Integer , primary_key=True)
    nome = db.column(db.String(100))
    cpf= db.column(db.String(11))
    ganero= db.column(db.String(16))
    idade = db.column(db.Integer)
    pedidos = db.relationship("entrega", backref="cliente")
    supermercados = db.relationship("supermercado", secondary = "cliente_supermercado", backref="clientes")
    suporte = db.relationship("suporte", backref="cliente")

    


