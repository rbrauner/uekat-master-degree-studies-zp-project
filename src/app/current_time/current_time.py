from fastapi import APIRouter
from datetime import datetime

current_time_router = APIRouter()


@current_time_router.get("/current-time")
async def current_time():
    now = datetime.now()

    return {
        "time": now.strftime("%H:%M:%S"),
    }
