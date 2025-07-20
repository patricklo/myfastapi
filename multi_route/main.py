import uvicorn
from fastapi import FastAPI
from todos import router as todos_router
from users import router as users_router

app = FastAPI()

app.include_router(todos_router, prefix="/todos", tags=["todos"])
app.include_router(users_router, prefix="/users", tags=["users"])

@app.get("/", tags=["home"])
def index():
    return "hello fastappi"

if __name__ == "__main__":
    uvicorn.run(app, port=8888)
