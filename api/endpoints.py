from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from database import crud
from fastapi.responses import HTMLResponse

router = APIRouter()


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True  # Позволяет возвращать ORM-объекты


@router.post("/users", response_model=UserOut)
async def create_user_endpoint(user: UserCreate):
    try:
        new_user = await crud.create_user(name=user.name, email=user.email, password_hash=user.password)
        return new_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/users", response_model=list[UserOut])
async def list_users():
    try:
        users = await crud.get_all_users()
        return users
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_class=HTMLResponse)
async def root():
    return "<h1>Finance App</h1>"
