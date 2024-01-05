from fastapi import FastAPI
from routers.predict import router as predict_router


app = FastAPI()

app.include_router(
    router = predict_router,
    prefix = '/predict',
)
