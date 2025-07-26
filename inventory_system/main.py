import uvicorn
from fastapi import FastAPI
from router_goods import router as goods_router
from router_warehouse import router as warehouse_router

app = FastAPI()

app.include_router(warehouse_router, prefix="/warehouse", tags=["warehouse"])
app.include_router(goods_router, prefix="/goods", tags=["goods"])

@app.get("/", tags=["home"])
def index():
    return "hello fast api"


from tortoise.contrib.fastapi import  register_tortoise

register_tortoise(
    app,
    db_url="mysql://root:changeit@localhost:3306/mytestdb",
    modules={"models":["models"]},
    generate_schemas=False,
    add_exception_handlers=True

)

if __name__ == "__main__":
    uvicorn.run(app, port=8888)