from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.controllers.pessoa_controller import PessoaController


router = APIRouter()
controller = PessoaController()


class LoginEntrada(BaseModel):
    email: str
    senha: str


@router.post("/api/login")
def login(dados: LoginEntrada):
    resultado = controller.login(dados.email, dados.senha)

    if resultado is None:
        raise HTTPException(
            status_code=401,
            detail="E-mail ou senha inválidos."
        )

    return resultado