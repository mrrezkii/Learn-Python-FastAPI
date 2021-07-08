from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data' : {'name': 'Muhammad Rezki Ananda'}}

@app.get('/about')
def about():
    return {'data' : {'about page'}}