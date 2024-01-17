from fastapi import FastAPI
from routers.predict import router as predict_router
from auth.auth import router as auth_router

app = FastAPI()

app.include_router(
    router = predict_router,
    prefix = '/predict',
)

app.include_router(auth_router)

