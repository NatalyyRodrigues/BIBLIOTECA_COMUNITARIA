from fastapi import APIRouter, HTTPException
from app.controllers.emprestimo_controller import EmprestimoController
from app.routes.livro_routes import livros
from pydantic import BaseModel
from app.models.conflito import ConflitoEstadoError

router = APIRouter()
controller = EmprestimoController(livros)

class EmprestimoEntrada(BaseModel):
    livro_id: int
    pessoa_id: int
    data: str


@router.get("/api/pessoas/{pessoa_id}/emprestimos")
def listar_emprestimos_por_pessoa(pessoa_id: int):
    pessoa = controller._buscar_pessoa(pessoa_id)

    if pessoa is None:
        raise HTTPException(
            status_code=404,
            detail="Pessoa não encontrada."
        )

    return controller.listar_emprestimos_por_pessoa(pessoa_id)



@router.post("/api/emprestimos", status_code=201)
def registrar_emprestimo(dados: EmprestimoEntrada):
    try:
        return controller.registrar_emprestimo(
            livro_id=dados.livro_id,
            pessoa_id=dados.pessoa_id,
            data=dados.data
        )

    except ConflitoEstadoError as erro:
        raise HTTPException(
            status_code=409,
            detail=str(erro)
        )

    except ValueError as erro:
        mensagem = str(erro)

        if mensagem == "A pessoa atingiu o limite de empréstimos.":
            raise HTTPException(
                status_code=409,
                detail=mensagem
            )

        raise HTTPException(
            status_code=404,
            detail=mensagem
        )