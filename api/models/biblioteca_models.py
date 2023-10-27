from api import db

class BibliotecaModels(db.Model):
    __tablename__ = "biblioteca"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    livro = db.Column(db.String(50), nullable=False)
    autor = db.Column(db.String(20), nullable=False)
    ano_publicacao = db.Column(db.Integer, nullable=False)