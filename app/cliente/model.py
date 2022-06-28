from sqlalchemy import PrimaryKeyConstraint, true
from app.extensions import db
from app.model import basemodel

class cliente(basemodel):
    __tablename__ = "cliente"

    id = db.Column(db.Integer, Primary_Key= True)
    nome = db.column(db.String(100))
    cpf= db.column(db.String(11))
    valorcompra = db.column(db.Floating)

    pass


