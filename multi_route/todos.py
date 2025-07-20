from typing import List

from fastapi import  APIRouter
from pydantic import BaseModel

router = APIRouter()

class Todo(BaseModel):
    id:int
    name: str
    finished: bool

@router.get("/")
async def all() -> List[Todo]:
    return [Todo(id=101, name="name1", finished="false"), Todo(id=102, name="name2", finished="false")]
