from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.todo._todo import todo_router
from api.v1.user._user import user_router

app: FastAPI = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(_create.create_route, 
#                    prefix="/user", 
#                    tags=["user"], 
#                    responses={404: {"description": "Not found"}},)

app.include_router(
    user_router, 
    prefix="/user", 
    tags=["users"]
)
app.include_router(
    todo_router,
    prefix="/todo",
    tags=["todos"],
)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}