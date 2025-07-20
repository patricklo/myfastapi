#Pydantic是一个用来执行数据定义、校验和转换的python库
#在真实调用api时，pydantic模型会起到类型校验和数据转换和文档生成能力

from typing import Annotated
import uvicorn
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id}
    if item:
        results.append({"item":item})
    return results

if __name__ == "__main__":
    uvicorn.run(port=8888)