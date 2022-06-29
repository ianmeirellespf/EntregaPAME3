from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

entrega_api = Blueprint("entrega_api", __name__)

class entrega(BaseModel):
    __tablename__ = "entrega"

    id = db.Column(db.Integer, Primary_Key= True)
    valor = db.column(db.Floating)
    data= db.column(db.String(16))
    produtos = db.column(db.Integer)
    entregador = db.column(db.Integer, db.ForeignKey("entregador.id"))
    endereçõ = db.column(db.String(100))
    cliente = db.column(db.Integer, db.ForeignKey("cliente.id"))
    