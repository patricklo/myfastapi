from fastapi import APIRouter, HTTPException
from models import Warehouse
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

@router.get("/")
def index():
    return "hello warehouse"


@router.get("/warehouses/")
async def get_warehouses():
    warehouses = await Warehouse.all()
    return warehouses


class WarehouseCreate(BaseModel):
    name: str

@router.post("/warehouses/")
async  def create_warehouse(warehouse: WarehouseCreate):
    new_warehouse = await Warehouse.create(name=warehouse.name, created_at=datetime.now())
    return new_warehouse

@router.delete("/warehouses/{warehouse_id")
async def delete_warehouse(warehouse_id: int):
    warehouse = await Warehouse.get_or_none(id=warehouse_id)
    if not warehouse:
        raise HTTPException(status_code=404, detail="unable to find record")
    await warehouse.delete()
    return {"message":"delete successfully"}
