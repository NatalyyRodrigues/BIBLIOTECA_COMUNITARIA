from app.models.emprestimo import Emprestimo, carregar_emprestimos
from app.models.livro import carregar_livros
from app.models.pessoa import carregar_pessoas


class EmprestimoController:
    def __init__(self, livros=None):
        if livros is None:
            livros = carregar_livros()

        self._livros = livros
        self._emprestimos = carregar_emprestimos(self._livros)
        self._pessoas = carregar_pessoas()

    def _para_dicionario(self, emprestimo):
        return {
            "id": emprestimo.mostrar_id(),
            "livro_id": emprestimo.mostrar_livro().mostrar_id(),
            "pessoa_id": emprestimo.mostrar_pessoa().mostrar_id(),
            "data": emprestimo.mostrar_data()
        }

    def listar_emprestimos_por_pessoa(self, pessoa_id):
        return [
            self._para_dicionario(emprestimo)
            for emprestimo in self._emprestimos
            if emprestimo.mostrar_pessoa().mostrar_id() == pessoa_id
        ]

    def _buscar_pessoa(self, pessoa_id):
        for pessoa in self._pessoas:
            if pessoa.mostrar_id() == pessoa_id:
                return pessoa

        return None

    def _buscar_livro(self, livro_id):
        for livro in self._livros:
            if livro.mostrar_id() == livro_id:
                return livro

        return None

    

    def registrar_emprestimo(self, livro_id, pessoa_id, data):
        livro = self._buscar_livro(livro_id)
        pessoa = self._buscar_pessoa(pessoa_id)

        if livro is None:
            raise ValueError("Livro não encontrado.")

        if pessoa is None:
            raise ValueError("Pessoa não encontrada.")

        quantidade_emprestimos = sum(
            1
            for emprestimo in self._emprestimos
            if emprestimo.mostrar_pessoa().mostrar_id() == pessoa_id
        )

        if quantidade_emprestimos >= pessoa.limite_emprestimos():
            raise ValueError("A pessoa atingiu o limite de empréstimos.")

        novo_id = max(
            (emprestimo.mostrar_id() for emprestimo in self._emprestimos),
            default=0
        ) + 1

        novo_emprestimo = Emprestimo(
            id=novo_id,
            livro=livro,
            pessoa=pessoa,
            data=data
        )

        livro.marcar_emprestado()
        self._emprestimos.append(novo_emprestimo)

        return self._para_dicionario(novo_emprestimo)

