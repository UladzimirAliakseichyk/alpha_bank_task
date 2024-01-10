from fastapi import FastAPI, Depends, HTTPException, status
from routers.predict import router as predict_router
from auth.auth import router as auth_router
from starlette import status
from auth.auth import get_current_user
from typing import Annotated

app = FastAPI()

app.include_router(
    router = predict_router,
    prefix = '/predict',
)

app.include_router(auth_router)

