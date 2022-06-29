from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

produto_api = Blueprint("produto_api", __name__)

class produto(BaseModel):
    __tablename__ = "produto"
    
    id = db.Column(db.Integer, Primary_Key= True)
    nome = db.column(db.String(50))
    valor = db.column(db.Floating)
    estoque= db.column(db.Integer)
    entregadaspresente = db.column(db.integer)
    validade = db.column(db.String(16))