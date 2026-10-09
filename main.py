from fastapi import FastAPI

from app.routes.livro_routes import router as livro_router
from app.routes.emprestimo_routes import router as emprestimo_router
from app.routes.pessoa_routes import router as pessoa_router


app = FastAPI(title="Biblioteca Comunitária API", version="1.0")

app.include_router(livro_router)
app.include_router(emprestimo_router)
app.include_router(pessoa_router)


@app.get("/")
def raiz():
    return {"api": "BIBLIOTECA_COMUNITARIA", "docs": "/docs"}