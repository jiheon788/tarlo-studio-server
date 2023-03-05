from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tarlo import t2i

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "tarlo server open"}


@app.get("/designs/")
async def root(text: str, size: int):
    return t2i(text, size)
