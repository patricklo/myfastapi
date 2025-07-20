from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int
    gender: str

mock_datas = [
    {"id": 1001, "name": "name1", "age": 24, "gender": "male"},
    {"id": 1002, "name": "name2", "age": 25, "gender": "female"},
    {"id": 1003, "name": "name3", "age": 26, "gender": "female"},
]

@app.get("/user/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in mock_datas:
        if user_id == user["id"]:
            return user
from typing import Annotated
from fastapi import Query

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3)] = None):
    return {"q": q}

if __name__  == "__main__":
    uvicorn.run(app, port=8888)