from api import ma
from..models import biblioteca_models
from marshmallow import fields

class BibliotecaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = biblioteca_models.BibliotecaModels
        load_instance = True
        fields = ('id', 'livro', 'autor', 'ano_publicacao')

    livro = fields.String(required=True)
    autor = fields.String(required=True)
    ano_publicacao = fields.Integer(required=True)
