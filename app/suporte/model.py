from app.extensions import db
from app.model import BaseModel
from flask import Blueprint



suporte_api = Blueprint("suporte_api", __name__)

class suporte(BaseModel):
    __tablename__ = "suporte"

    id = db.Column(db.Integer, Primary_Key= True)
    data = db.column(db.String(16))
    ajuda = db.column(db.String(100))
    satisfação = db.column(db.Integer)
    cliente = db.column(db.Integer, db.ForeignKey("cliente.id"))