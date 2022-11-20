from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import bcrypt

current_time_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

users_db = {
    "test": {
        "username": "test",
        "full_name": "Test",
        "email": "test@eukat.edu.pl",
        "hashed_password": "$2b$12$kNA1nFAWJ2.20xtgxIPEjewx61nK4iqffNPZKPA8hXJncTNRAAaGS", # zaq1@WSX
        "disabled": False,
    },
    "test2": {
        "username": "test2",
        "full_name": "Test 2",
        "email": "test2@eukat.edu.pl",
        "hashed_password": "$2b$12$UlDtIjdmQzlrQ2vZiXeN/uF5tjLfmH2CLQrUV/sfDg3FP/ZpGOdaG", # cde3$RFV
        "disabled": True,
    },
}

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return User(**user_dict)

def decode_token(token):
    user = get_user(users_db, token)
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

@current_time_router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = User(**user_dict)
    if not bcrypt.checkpw(form_data.password.encode('utf-8'), user.hashed_password.encode('utf-8')):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    if user.disabled:
        raise HTTPException(status_code=401, detail="Disabled user")

    return {"access_token": user.username, "token_type": "bearer"}

@current_time_router.get("/current-time")
async def current_time(current_user: User = Depends(get_current_user)):
    now = datetime.now()

    return {
        "time": now.strftime("%H:%M:%S"),
    }
