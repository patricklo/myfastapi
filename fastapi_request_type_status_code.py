import uvicorn
from fastapi import FastAPI, status

app = FastAPI()

@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}

if __name__ == "__main__":
    uvicorn.run(app=app, port=8888)