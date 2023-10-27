from api import api
from flask_restful import Resource
from..schemas import biblioteca_schemas
from api.entidades.entidades import Biblioteca
from..services import biblioteca_services
from flask import request, make_response, jsonify

class BibliotecaViews(Resource):
    def post(self):
        validador_livro = biblioteca_schemas.BibliotecaSchema()
        validate = validador_livro.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            livro = request.json['livro']
            autor = request.json['autor']
            ano_publicacao = request.json['ano_publicacao']
        novo_livro = Biblioteca(livro=livro,
                                    autor=autor,
                                    ano_publicacao=ano_publicacao)
        resultado = biblioteca_services.cadastro_livros(novo_livro)
        x = validador_livro.jsonify(resultado)
        return make_response(x, 201)


    def get(self):
        livro = biblioteca_services.listagem_livros()
        lv = biblioteca_schemas.BibliotecaSchema(many=True)
        return make_response(lv.jsonify(livro), 200)

class BibliotecaDetalhes(Resource):

    def get(self, id):
        livro = biblioteca_services.listagem_livros_id(id)
        if livro is None:
            return make_response(jsonify("Livro não encontrado"), 404)
        lv = biblioteca_schemas.BibliotecaSchema()
        return make_response(lv.jsonify(livro), 200)

    def put(self, id):
        livro_antigo = biblioteca_services.listagem_livros_id(id)
        if livro_antigo is None:
            return make_response(jsonify("Livro não encontrado"), 404)
        lv = biblioteca_schemas.BibliotecaSchema()
        validate = lv.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            livro = request.json['livro']
            autor = request.json['autor']
            ano_publicacao = request.json['ano_publicacao']

            novo_livro = Biblioteca(livro=livro,
                                    autor=autor,
                                    ano_publicacao=ano_publicacao)
            biblioteca_services.atualizar_livro(livro_antigo, novo_livro)
            livro_atualizado = biblioteca_services.listagem_livros_id(id)
            return make_response(lv.jsonify(livro_atualizado), 200)

    def delete(self, id):
        livro = biblioteca_services.listagem_livros_id(id)
        if livro is None:
            return make_response(jsonify("Livro não encontrado!"), 404)
        biblioteca_services.deletar_livro(livro)
        return make_response(jsonify("Livro excluído"), 200)

api.add_resource(BibliotecaViews, '/biblioteca')
api.add_resource(BibliotecaDetalhes, '/biblioteca/<int:id>')