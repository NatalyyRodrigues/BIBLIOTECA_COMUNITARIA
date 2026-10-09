
from app.models.livro import Livro, carregar_livros
from app.models.pessoa import Leitor, Bibliotecario, carregar_pessoas
from app.models.emprestimo import carregar_emprestimos
from app.models.conflito import ConflitoEstadoError

from app.controllers.livro_controller import LivroController
from app.controllers.emprestimo_controller import EmprestimoController
from app.controllers.pessoa_controller import PessoaController


total = 0


def verificar(descricao, condicao):
    global total
    assert condicao, f"FALHOU: {descricao}"
    total += 1
    print(f"OK {total}: {descricao}")


print("=== TESTES DA BIBLIOTECA COMUNITÁRIA ===")

# 1. Carregamento de livros
livros = carregar_livros()
verificar("Carregamento de 5 livros", len(livros) >= 5)

# 2. Livro disponível
livro = livros[0]
verificar("Livro inicialmente disponível", livro.mostrar_disponivel())

# 3. Marcar livro como emprestado
livro.marcar_emprestado()
verificar("Livro marcado como emprestado", livro.mostrar_emprestado())

# 4. Impedir empréstimo duplicado
conflito_detectado = False

try:
    livro.marcar_emprestado()
except ConflitoEstadoError:
    conflito_detectado = True

verificar("Impedir empréstimo duplicado", conflito_detectado)

# 5. Título vazio
titulo_invalido = False

try:
    Livro(10, "", "Autor Teste", 2020)
except ValueError:
    titulo_invalido = True

verificar("Rejeitar título vazio", titulo_invalido)

# 6. Ano futuro
ano_invalido = False

try:
    Livro(11, "Livro Teste", "Autor Teste", 3000)
except ValueError:
    ano_invalido = True

verificar("Rejeitar ano futuro", ano_invalido)

# 7. Carregamento de pessoas
pessoas = carregar_pessoas()
verificar("Carregamento de 5 pessoas", len(pessoas) >= 5)

# 8. Limite do leitor
leitor = Leitor(20, "Leitor Teste", "leitor@teste.com", "1234")
verificar("Leitor possui limite de 3 empréstimos", leitor.limite_emprestimos() == 3)

# 9. Limite do bibliotecário
bibliotecario = Bibliotecario(
    21, "Bibliotecário Teste", "bibliotecario@teste.com", "1234"
)
verificar(
    "Bibliotecário possui limite de 10 empréstimos",
    bibliotecario.limite_emprestimos() == 10
)

# 10. Permissão do bibliotecário
verificar(
    "Bibliotecário pode cadastrar livros",
    bibliotecario.pode_cadastrar_livro()
)

# 11. Restrição do leitor
verificar(
    "Leitor não pode cadastrar livros",
    not leitor.pode_cadastrar_livro()
)

# 12. Carregamento dos empréstimos
emprestimos = carregar_emprestimos()
verificar("Carregamento de empréstimos", len(emprestimos) >= 2)

# 13. Consulta de livros disponíveis
livro_controller = LivroController()
disponiveis = livro_controller.listar_disponiveis()

verificar(
    "Listar somente livros disponíveis",
    len(disponiveis) > 0
    and all(not livro["emprestado"] for livro in disponiveis)
)

# 14. Consulta de empréstimos por pessoa
emprestimo_controller = EmprestimoController()
emprestimos_pessoa = emprestimo_controller.listar_emprestimos_por_pessoa(1)

verificar(
    "Consultar empréstimos por pessoa",
    len(emprestimos_pessoa) == 2
    and all(e["pessoa_id"] == 1 for e in emprestimos_pessoa)
)

# 15. Autenticação
pessoa_controller = PessoaController()
resultado_login = pessoa_controller.login(
    "rodrigo.leitor@bairro.com", "4567"
)

verificar(
    "Autenticar leitor com credenciais válidas",
    resultado_login is not None
    and resultado_login["perfil"] == "leitor"
)

print(f"\n=== {total} TESTES APROVADOS ===")
