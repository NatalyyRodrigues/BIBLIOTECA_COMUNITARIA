from app.models.livro import carregar_livros

class LivroController:
    def __init__(self, livros=None):
        if livros is None:
            livros = carregar_livros()

        self._livros = livros

    def _para_dicionario(self, livro):
        return {
            "id": livro.mostrar_id(),
            "titulo": livro.mostrar_titulo(),
            "autor": livro.mostrar_autor(),
            "ano_publicacao": livro.mostrar_ano_publicacao(),
            "emprestado": livro.mostrar_emprestado()
        }

    def listar_livros(self):
        resultado = []

        for livro in self._livros:
            dicionario = self._para_dicionario(livro)
            resultado.append(dicionario)

        return resultado

    def listar_disponiveis(self):
        return [
            self._para_dicionario(livro)
            for livro in self._livros
            if not livro.mostrar_emprestado()
        ]

    def buscar_livro_por_id(self, id):
        for livro in self._livros:
            if livro.mostrar_id() == id:
                return self._para_dicionario(livro)

        return None