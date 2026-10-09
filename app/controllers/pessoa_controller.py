from app.models.pessoa import carregar_pessoas

class PessoaController:
    def __init__(self):
        self._pessoas = carregar_pessoas()

    def login(self, email, senha):
        for pessoa in self._pessoas:
            if pessoa.mostrar_email() == email and pessoa.autenticar(senha):
                return {
                    "id": pessoa.mostrar_id(),
                    "nome": pessoa.mostrar_nome(),
                    "perfil": pessoa.mostrar_perfil(),
                    "permissoes": pessoa.permissoes()
                }

        return None