from fastapi import APIRouter, HTTPException
from app.controllers.livro_controller import LivroController
from app.models.livro import carregar_livros

router = APIRouter()

livros = carregar_livros()
controller = LivroController(livros)

@router.get("/api/livros")
def listar_livros():
    return controller.listar_livros()

@router.get("/api/livros/disponiveis")
def listar_disponiveis():
    return controller.listar_disponiveis()

@router.get("/api/livros/{id}")
def buscar_livro(id: int):
    livro = controller.buscar_livro_por_id(id)

    if livro is None:
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado"
        )

    return livro