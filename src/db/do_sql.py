import asyncio

from sqlmodel import Session
from sqlmodel import SQLModel

from src.db.fake_data import get_list_of_stocks
from  src.models.stock_model import Stock
from src.db.connect_cfg_db import get_session, engine_cfg
'''
#Crete Tables
SQLModel.metadata.create_all(engine_cfg)
'''
async def get_db_lis():
    lis_db=  await get_list_of_stocks()
    return lis_db
async def add_and_commit() :
    with Session(engine_cfg) as session:
        for st in await get_db_lis():
                db_st = Stock.model_validate(st)
                session.add(  db_st )
        session.commit()

asyncio.run(add_and_commit())
