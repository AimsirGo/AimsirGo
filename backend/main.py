//testing

from fastapi import FastAPI

app = FastAPI(title="AimsirGo API")

@app.get("/")
def read_root():
    return {"status": "ok", "project": "AimsirGo", "team": "Node4"}
