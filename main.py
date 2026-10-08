from fastapi import FastAPI


app = FastAPI(title='Biblioteca Comunitária API', version='1.0')

@app.get('/')
def raiz():
    return{'api': 'BIBLIOTECA_COMUNITARIA', 'docs': '/docs'}