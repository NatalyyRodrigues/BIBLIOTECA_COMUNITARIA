## PROJETO BIBLIOTECA COMUNITÁRIA 
# NATALY GABRIELY E DEBORA MIRANDA

Sistema de controle de acervo e empréstimos de um ponto de leitura de bairro.
O sistema garante:

1. Controle do acervo (livros e se estão disponíveis).
2. Registro de empréstimos (quem pegou qual livro e quando).
3. Limites diferentes: leitor até 3 empréstimos ativos; bibliotecário até 10.
4. Regras de Negócio: Não emprestar livro já emprestado; ano de publicação válido; só quem tem permissão `cadastrar_livro` inclui livro novo.

## DESENVIMENTO DA ARQUITETURA MVC E CONFIGURANDO O AMBIENTE FastAPI
1. Criado os arquivos da arquitetura MVC: app > controllers> data > models > routes.
2. Criado o ambiente virtual utilizando o comando python -m venv venv e ativando o ambiente com o comando venv\Scripts\activate.
3. Realizado a instação do framework FastAPI comando (pip install fastapi uvicorn[standard]) e criado  o congelamento de dependências com o comando (pip freeze > requirements.txt ).
4. Por último, realizado a instalção do pacote de dependências utilizando o comando ip install -r requirements.txt.


## DIAGRAMA DE CLASSES
O diagrama abaixo representa a estrutura do sistema Biblioteca Comunitária, incluindo as classes Livro, Emprestimo e Pessoa, além das especializações Leitor e Bibliotecario.

![Diagrama de Classes](docs/diagrama_classes.png)

## IMPLEMENTAÇÕES

1. Implementação dos dados mockados de emprestimo, livro e pessoas na camada data.
2. Implementação na camada model, criando os arquivos  pessoa.py, livro.py, conflito.py contendo as classes e seus métodos e seus parâmetros.
3. Camadas model: arquivo pessoa.py foi implementado a classe principal pessoa e suas subclasses bibliotecario e leitor.
4. Implementação dos arquivos __init__.py em cada arquivo do app seguindo a documentação do trabalho.

## CONTROLLERS 

1. Camada que administra as camadas models e mocks; devolve listas/dicionários para a API.
2. livro_controller.py: lista todo o acervo, lista só livros disponíveis e busca livro por ID (serializa objeto Livro em dict).
3. emprestimo_controller.py: carrega empréstimos iniciais; lista empréstimos por pessoa; registra empréstimo (valida livro/pessoa, limite por perfil, cria registro, marca livro emprestado). Usa ValueError (não encontrado / limite) e deixa conflitos do livro para ConflitoEstadoError no model.
4. pessoa_controller.py: login por e-mail e senha; retorna id, nome, perfil e permissões, ou falha na autenticação.

## VERIFICAR:
*Realiza as seguintes validações (sem subir a API):
1. Carregamento de livros e pessoas (mocks)
2. Disponibilidade e empréstimo de livro; bloqueio de empréstimo duplicado (ConflitoEstadoError)
3. Rejeição de título vazio e ano futuro (ValueError)
4. Limites: leitor (3) e bibliotecário (10); permissão cadastrar_livro
5. Carregamento de empréstimos
6. LivroController: listar disponíveis
7. EmprestimoController: empréstimos por pessoa
8. PessoaController: login com credenciais válidas
9. Se tudo passar, exibe quantos testes foram aprovados.

Estrutura realizada: routes → controllers → models + data (mocks); erros de negócio nos models/controllers; HTTP apenas nas routes.

COMANDO PARA EXECUTAR O CÓDIGO: uvicorn main:app --reload
SERVIDOR PROJETO:  http://127.0.0.1:8000/docs 

