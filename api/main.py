from fastapi import FastAPI
from api.v1.user import _router
from database._database import Base

app: FastAPI = FastAPI()

# app.include_router(router.router)
# app.include_router(_router.router)
app.include_router(_router.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}