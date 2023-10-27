from..models import biblioteca_models
from api import db

def cadastro_livros(produto):
    livro = biblioteca_models.BibliotecaModels(livro=produto.livro,
                                               autor=produto.autor,
                                               ano_publicacao=produto.ano_publicacao)
    db.session.add(livro)
    db.session.commit()
    return livro

def listagem_livros():
    livro = biblioteca_models.BibliotecaModels.query.all()
    return livro

def listagem_livros_id(id):
    livro = biblioteca_models.BibliotecaModels.query.filter_by(id=id).first()
    return livro
def atualizar_livro(livro_antigo, livro_novo):
    livro_antigo.livro = livro_novo.livro
    livro_antigo.autor = livro_novo.autor
    livro_antigo.ano_publicacao = livro_novo.ano_publicacao
    db.session.commit()

def deletar_livro(id):
    db.session.delete(id)
    db.session.commit()