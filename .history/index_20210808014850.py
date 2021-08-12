from fastapi import FastAPI
from googlesearch import search

app = FastAPI()

app.get('/pesq/{q}{n}{lg=en}')
def pesq(q:str):
    return search(term=q,num_results=n,lang=lg)