import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Query

app = FastAPI()

def get_current_user():
    return {"username":"admin"}

@app.get("/items/")
def read_items(current_user: dict = Depends(get_current_user)):
    return {"user": current_user, "items":["item2","item2"]}

def pagination_params(page_number: int = Query(1, ge=1),
                       page_size: int = Query(10, ge=1, le=100)):
    return {"page_number": page_number, "page_size": page_size}

@app.get("/items2/")
def read_items(pagination: dict = Depends(pagination_params)):
    page_number = pagination["page_number"]
    page_size = pagination["page_size"]

    return {"page_number": page_number, "page_size": page_size}

if __name__ == "__main__":
    uvicorn.run(app, port=8888)