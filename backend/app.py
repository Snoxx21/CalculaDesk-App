from fastapi import FastAPI
from cas_worker import CASWorker
app = FastAPI()
@app.post('/api/solve-text')
async def solve_text(q: dict):
    w = CASWorker()
    return {'steps': w.solve_from_text(q.get('text',''))}
