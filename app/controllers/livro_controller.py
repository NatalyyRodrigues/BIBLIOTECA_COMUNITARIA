from app.models.livro import carregar_livros

class LivroController:
    def __init__(self):
        self._livros = carregar_livros()

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