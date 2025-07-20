from typing import List

from fastapi import  APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    id:int
    name: str

@router.get("/")
async def all() -> List[User]:

    return [User(id=101, name="name1"), User(id=102, name="name2")]
