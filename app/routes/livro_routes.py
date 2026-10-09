from fastapi import APIRouter
from app.controllers.livro_controller import LivroController

router = APIRouter()
controller = LivroController()

@router.get("/api/livros")
def listar_livros():
    return controller.listar_livros()