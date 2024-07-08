from fastapi import APIRouter
from schemas.users import User
from crud.users_crud import new_user, see_users



users_router = APIRouter()


@users_router.post('/users')
async def new_user(user:User):
    return new_user(user)


@users_router.get('/users')
async def get_users():
    return see_users




