from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .base import ModeloBase
from .usuarios import Usuario
from .tarefas import Tarefa

__all__ = ["db", "ModeloBase", "Usuario", "Tarefa"]