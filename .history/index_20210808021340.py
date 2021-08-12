import uvicorn
from fastapi import FastAPI,Request
from googlesearch import search

app = FastAPI()

app.get('/')
def start(request:Request):
    ip = request.client
    return {'ip'}

app.get('/pesq/{q}')
def pesq(q:str,n:int=10,lg:str='en'):
    return search(term=q,num_results=n,lang=lg)

uvicorn.run(app,host='0.0.0.0',port=8000)