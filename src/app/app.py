from fastapi import FastAPI
from src.app.prime.prime import prime_router
from src.app.picture_invert.picture_invert import picture_invert_router

app = FastAPI()
app.include_router(prime_router)
app.include_router(picture_invert_router)
