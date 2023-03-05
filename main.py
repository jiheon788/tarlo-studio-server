from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "tarlo server open"}


@app.get("/designs")
async def root():
    return {"message": "tarlo server open"}
