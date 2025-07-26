from fastapi import APIRouter, HTTPException, Query
from models import Goods

router = APIRouter()


@router.get("/")
def index():
    return "hello goods"


@router.get("/goods/")
async def get_goods():
    goods = await Goods.all()
    return goods


@router.get("/goods/")
async def get_goods(
        warehouse_id: int = Query(None, description="warehouse id"),
        warehouse_name: str = Query(None, description="warehouse name"),
        min_quantity: int = Query(None, description="quantity greater than"),
        keyword: str = Query(None, description="name contains keyword")
):
    query = Goods.all()
    if warehouse_id:
        query = query.filter(warehouse_id=warehouse_id)
    if warehouse_name:
        query = query.filter(warehouse__name__icontains=warehouse_name)
    if min_quantity:
        query = query.filter(quantity__gt=min_quantity)
    if keyword:
        query = query.filter(name__icontains=keyword)

    results = await query

    return results
