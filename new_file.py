from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Hello, World!'}


@app.get('/test')
def read_custom():
    return {'message': 'Website!'}


@app.get('/hello')
def read_hello():
    return {'message': 'Hello from the last page!'}
