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

user_depencency = Annotated[dict, Depends(get_current_user)]

@app.get('/get_user', status_code=status.HTTP_200_OK)
async def user(user: user_depencency):
    if user is None:
        print(user)
        raise HTTPException(status_code=401, detail='Authentication Faild')
    return {'User': user['username']}