from app.data.emprestimo_mock import EMPRESTIMOS
from app.models.livro import carregar_livros
from app.models.pessoa import carregar_pessoas

class Emprestimo:
    def __init__(self, id, livro, pessoa, data):
        self._id = id
        self._livro = livro
        self._pessoa = pessoa
        self._data = data

    def mostrar_id(self):
        return self._id

    def mostrar_livro(self):
        return self._livro

    def mostrar_pessoa(self):
        return self._pessoa

    def mostrar_data(self):
        return self._data

    def __repr__(self):
        return f"Emprestimo(id={self._id}, livro={self._livro.mostrar_titulo()!r})"

def carregar_emprestimos(livros=None):
    emprestimos = []

    if livros is None:
        livros = carregar_livros()

    pessoas = carregar_pessoas()

    for emprestimo in EMPRESTIMOS:
        livro_encontrado = None

        for livro in livros:
            if livro.mostrar_id() == emprestimo["livro_id"]:
                livro_encontrado = livro
                break

        pessoa_encontrada = None
        for pessoa in pessoas:
            if pessoa.mostrar_id() == emprestimo["pessoa_id"]:
                pessoa_encontrada = pessoa
                break

        if livro_encontrado is None or pessoa_encontrada is None:
            raise ValueError("Livro ou pessoa não encontrado.")

        novo_emprestimo = Emprestimo(
            id=emprestimo["id"],
            livro=livro_encontrado,
            pessoa=pessoa_encontrada,
            data=emprestimo["data"]
            )
        emprestimos.append(novo_emprestimo)

    return emprestimos
    

        
