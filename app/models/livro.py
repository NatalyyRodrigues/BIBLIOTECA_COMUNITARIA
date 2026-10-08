from datetime import date

from app.data.livro_mock import LIVROS
from app.models.conflito import ConflitoEstadoError


class Livro:
    def __init__(self, id, titulo, autor, ano_publicacao, emprestado=False):
        self._id = id
        self.alterar_titulo(titulo)
        self.alterar_autor(autor)
        self.alterar_ano_publicacao(ano_publicacao)
        self.alterar_emprestado(emprestado)

    def alterar_titulo(self, titulo):
        titulo = (titulo or "").strip()
        if not titulo:
            raise ValueError("O título não pode ser vazio.")
        self._titulo = titulo

    def alterar_autor(self, autor):
        autor = (autor or "").strip()
        if not autor:
            raise ValueError("O autor não pode ser vazio.")
        self._autor = autor

    def alterar_ano_publicacao(self, ano):
        ano = int(ano)
        ano_atual = date.today().year
        if ano > ano_atual:
            raise ValueError(
                f"O ano de publicação ({ano}) não pode ser maior que {ano_atual}."
            )
        if ano < 0:
            raise ValueError("O ano de publicação não pode ser negativo.")
        self._ano_publicacao = ano

    def alterar_emprestado(self, emprestado):
        self._emprestado = bool(emprestado)

    def mostrar_id(self):
        return self._id

    def mostrar_titulo(self):
        return self._titulo

    def mostrar_autor(self):
        return self._autor

    def mostrar_ano_publicacao(self):
        return self._ano_publicacao

    def mostrar_emprestado(self):
        return self._emprestado

    def mostrar_disponivel(self):
        return not self._emprestado

    def marcar_emprestado(self):
        if self._emprestado:
            raise ConflitoEstadoError("Este livro já está emprestado.")
        self._emprestado = True

    def __repr__(self):
        return (
            f"Livro(id={self._id}, titulo={self._titulo!r}, "
            f"emprestado={self._emprestado})"
        )


def carregar_livros():
    livros = []
    for registro in LIVROS:
        livros.append(
            Livro(
                id=registro["id"],
                titulo=registro["titulo"],
                autor=registro["autor"],
                ano_publicacao=registro["ano_publicacao"],
                emprestado=registro["emprestado"],
            )
        )
    return livros
