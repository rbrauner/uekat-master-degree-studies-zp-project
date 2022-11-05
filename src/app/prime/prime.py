from fastapi import APIRouter
import sympy

prime_router = APIRouter()

@prime_router.get("/prime/{number}")
async def create_user(number: int):
    isPrime = sympy.isprime(number)

    return {
        "isPrime": isPrime,
        "number": number,
    }