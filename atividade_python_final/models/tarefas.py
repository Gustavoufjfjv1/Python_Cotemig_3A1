from . import db
from .base import ModeloBase


class Tarefa(ModeloBase):
    __tablename__ = "tarefas"

    titulo = db.Column(db.String(60), nullable=False)
    descricao = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(80), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=True)

    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.titulo).all()