class Biblioteca:
    def __init__(self, livro, autor, ano_publicacao):
        self.__livro = livro
        self.__autor = autor
        self.__ano_publicacao = ano_publicacao

    @property
    def livro(self):
        return self.__livro
    @livro.setter
    def livro(self, novo_livro):
        self.__livro = novo_livro

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, novo_autor):
        self.__autor = novo_autor

    @property
    def ano_publicacao(self):
        return self.__ano_publicacao

    @ano_publicacao.setter
    def ano_publicacao(self, novo_ano_publicacao):
        self.__ano_publicacao = novo_ano_publicacao