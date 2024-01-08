from fastapi import FastAPI, Depends
from routers.predict import router as predict_router
from auth.auth import router as register_router
from starlette import status
from auth.auth import db_dependency, get_current_user
from typing import Annotated

app = FastAPI()

app.include_router(
    router = predict_router,
    prefix = '/predict',
)

app.include_router(
    router = register_router,
    prefix = '/token'
)
user_depencency = Annotated[dict, Depends(get_current_user)]

@app.get('/', status_code=status.HTTP_200_OK)
async def user(user: user_depencency):
    print(user)
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Faild')
    return {'User': user}