from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin


class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    senha = db.Column(db.String(150))
    nome = db.Column(db.String(150))
    tarefas = db.relationship('Tarefa')

    def __repr__(self):
        info = f"{self.id} | {self.email} | {self.nome}"
        if len(self.tarefas) > 0:
            info+= "\nAnotações..."
            for tarefa in self.tarefas:
                info+= tarefa.texto + "\n"
        return info

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(55))
    texto = db.Column(db.String(1000))
    data = db.Column(db.DateTime(timezone=True), default=func.now())
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    publica = db.Column(db.Boolean, default=False)
    status_id = db.Column(db.Integer, db.ForeignKey('estado.id'))
    
class Estado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(55))
    estados = db.relationship('Tarefa')