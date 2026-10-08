from app.data.pessoa_mock import PESSOAS


class Pessoa:
    """Classe base: dados comuns a quem usa a biblioteca."""

    LIMITE_EMPRESTIMOS = 0

    def __init__(self, id, nome, email, senha):
        self._id = id
        self.alterar_nome(nome)
        self.alterar_email(email)
        self.alterar_senha(senha)

    def alterar_nome(self, nome):
        nome = (nome or "").strip()
        if not nome:
            raise ValueError("O nome não pode ser vazio.")
        self._nome = nome

    def alterar_email(self, email):
        email = (email or "").strip()
        if "@" not in email:
            raise ValueError("E-mail inválido.")
        self._email = email

    def alterar_senha(self, senha):
        senha = (senha or "").strip()
        if len(senha) < 4:
            raise ValueError("A senha deve ter pelo menos 4 caracteres.")
        self._senha = senha

    def mostrar_id(self):
        return self._id

    def mostrar_nome(self):
        return self._nome

    def mostrar_email(self):
        return self._email

    def mostrar_senha(self):
        return self._senha

    def mostrar_perfil(self):
        return "pessoa"

    def limite_emprestimos(self):
        return self.LIMITE_EMPRESTIMOS

    def permissoes(self):
        return ["emprestar"]

    def pode_cadastrar_livro(self):
        return "cadastrar_livro" in self.permissoes()

    def autenticar(self, senha_informada):
        return self._senha == senha_informada

    def __repr__(self):
        return f"Pessoa(id={self._id}, nome={self._nome!r})"


class Leitor(Pessoa):
    LIMITE_EMPRESTIMOS = 3

    def mostrar_perfil(self):
        return "leitor"

    def __repr__(self):
        return f"Leitor(id={self._id}, nome={self._nome!r})"


class Bibliotecario(Pessoa):
    LIMITE_EMPRESTIMOS = 10

    def mostrar_perfil(self):
        return "bibliotecario"

    def permissoes(self):
        base = super().permissoes()
        return base + ["cadastrar_livro"]

    def __repr__(self):
        return f"Bibliotecario(id={self._id}, nome={self._nome!r})"


PERFIS = {
    "leitor": Leitor,
    "bibliotecario": Bibliotecario,
}


def carregar_pessoas():
    pessoas = []
    for registro in PESSOAS:
        perfil = registro["perfil"]
        classe = PERFIS[perfil]
        pessoas.append(
            classe(
                id=registro["id"],
                nome=registro["nome"],
                email=registro["email"],
                senha=registro["senha"],
            )
        )
    return pessoas
