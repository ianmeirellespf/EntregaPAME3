from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

entrega_api = Blueprint("entrega_api", __name__)

class entregaproduto(BaseModel):
    __tablename__ = "entrega_produto"

    id = db.Column(db.Integer , primary_key=True)

    entrega = db.Column(db.Integer , db.ForeignKey("entrega.id"))
    produto = db.Column(db.Integer , db.ForeignKey("produto.id"))
class entrega(BaseModel):

    __tablename__ = "entrega"

    id = db.Column(db.Integer , primary_key=True)
    valor = db.Column(db.Float)
    data= db.Column(db.Date)
    produtos = db.relationship("produto", secondary = "entrega_produto", backref="entregascontendo")
    entregador = db.Column(db.Integer, db.ForeignKey("entregador.id"))
    endereçõ = db.Column(db.String(100))
    demora= db.Column(db.Time)
    cliente = db.Column(db.Integer, db.ForeignKey("cliente.id"))
    