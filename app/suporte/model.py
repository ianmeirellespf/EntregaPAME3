from app.extensions import db
from app.model import BaseModel
from flask import Blueprint



suporte_api = Blueprint("suporte_api", __name__)

class suporte(BaseModel):
    __tablename__ = "suporte"

    id = db.Column(db.Integer , primary_key=True)
    data = db.Column(db.Date)
    resolvido = db.Column(db.Boolean)
    ajuda = db.Column(db.String(100))
    satisfação = db.Column(db.Integer)
    cliente = db.Column(db.Integer, db.ForeignKey("cliente.id"))