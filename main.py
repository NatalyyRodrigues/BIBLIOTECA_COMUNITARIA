from fastapi import FastAPI
from app.routes.livro_routes import router

app = FastAPI(title='Biblioteca Comunitária API', version='1.0')

app.include_router(router)

@app.get('/')
def raiz():
    return{'api': 'BIBLIOTECA_COMUNITARIA', 'docs': '/docs'}