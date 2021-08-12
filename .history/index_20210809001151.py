import uvicorn
from fastapi import FastAPI,Request
from googlesearch import search

from lib import get_music_yt as gm

app = FastAPI()

@app.get('/')
async def start(request:Request):
    port = request.client.host
    return {'ip':port}

@app.get('/pesq/{q}')
def pesq(q:str,n:int=10,lg:str='en'):
    return search(term=q,num_results=n,lang=lg)

@app.get('/yt/{m}')
def get_music(m:str):
    lyt = gm(m)
    return yt

uvicorn.run(app,host='0.0.0.0',port=8000)