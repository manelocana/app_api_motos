from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get():
    return "primer get"

@app.get("/")
async def get():
    return "primer get"