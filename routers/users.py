from fastapi import APIRouter, HTTPException
from schemas.users import User
from crud.users_crud import new_user



users_router = APIRouter()


@users_router.post('/users')
async def new_user(user:User):
    return new_user(user)





