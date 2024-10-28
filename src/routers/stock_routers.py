from fastapi import APIRouter, HTTPException, Query

from typing import Annotated

from sqlmodel import select

from ..db.connect_cfg_db import SessionDep
from ..models.hero_model import HeroBase, Hero, HeroUpdate
from ..models.stock_model import StockBase, Stock, StockUpdate

stock_router = APIRouter()
@stock_router.post("/addStock/", response_model=Stock)
async def create_stock(stock: StockBase, session: SessionDep):
    db_stock  = Stock.model_validate(stock)
    session.add(db_stock)
    session.commit()
    session.refresh(db_stock)
    return db_stock


@stock_router.get("/lisStock/", response_model=list[Stock])
async def read_stocks(
    session: SessionDep
    # offset: int = 0,
    # limit: Annotated[int, Query(le=100)] = 100,
):
    #stocks = session.exec(select(Stock).offset(offset).limit(limit)).all()
    stocks = session.exec(select(Stock)).all()
    return stocks


@stock_router.get("/stocks/{stk_id}", response_model=Stock)
async def read_stock(stk_id: int, session: SessionDep):
    st = session.get(Stock, stk_id)
    if not st:
        raise HTTPException(status_code=404, detail="Stock not found")
    return st


@stock_router.patch("/stock/{id}", response_model=Stock)
async def update_stock(id: int, in2Upd: StockUpdate, session: SessionDep):
    stk_db = session.get(Stock, id)
    if not stk_db:
        raise HTTPException(status_code=404, detail="Stock not found")

    stk_data = in2Upd.model_dump(exclude_unset=True)
    stk_db.sqlmodel_update(stk_data)
    session.add(stk_db)
    session.commit()
    session.refresh(stk_db)
    return stk_db


@stock_router.delete("/stocks/{stk_id}")
async def delete_stock(stk_id: int, session: SessionDep):
    stock = session.get(Stock, stk_id)
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    session.delete(stock)
    session.commit()
    return {"ok": True}

@stock_router.get("/select_stock/", response_model=list[Stock])
async def select_stock(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100, ) -> list[Stock]:
    stocks = session.exec(select(Stock).offset(offset).limit(limit)).all()
    return stocks
#-1 https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/create-and-update-relationships/#create-a-team-with-heroes

#-2 SSE Clinet  Event Hooks/httpx  https://www.python-httpx.org/advanced/event-hooks/
# #https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/back-populates/#read-data-objects fastapi Relationship fk

#https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html#selecting-orm-entities to try