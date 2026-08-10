from . import db
from .base import ModeloBase


class Usuario(ModeloBase):
    __tablename__ = "usuarios"

    nome = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    senha = db.Column(db.String(80), nullable=False)

    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.nome).all()