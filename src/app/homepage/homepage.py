from fastapi import APIRouter
from fastapi.responses import RedirectResponse

homepage_router = APIRouter()


@homepage_router.get("/")
async def homepage():
    return RedirectResponse("/docs")
