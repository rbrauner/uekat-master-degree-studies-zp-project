from fastapi import FastAPI
from src.app.prime.prime import prime_router

app = FastAPI()
app.include_router(prime_router)
