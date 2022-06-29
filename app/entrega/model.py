from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

entrega_api = Blueprint("entrega_api", __name__)

class entrega(BaseModel):

    __tablename__ = "entrega"

    id = db.Column(db.Integer , primary_key=True)
    valor = db.column(db.Float)
    data= db.column(db.String(16))
    produtos = db.column(db.Integer)
    entregador = db.column(db.Integer, db.ForeignKey("entregador.id"))
    endereçõ = db.column(db.String(100))
    cliente = db.column(db.Integer, db.ForeignKey("cliente.id"))
    