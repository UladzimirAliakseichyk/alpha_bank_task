from fastapi import FastAPI
from routers.predict import router as predict_router

from fastapi_users import FastAPIUsers
from models.models import User
from models.schemes import UserCreate, UserRead
from auth.manager import get_user_manager
from auth.auth import auth_backend


app = FastAPI()

app.include_router(
    router = predict_router,
    prefix = '/predict',
)


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)