from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional
import json
import aiofiles as aiof
from sqlmodel import SQLModel, Field

from src.cfg.cfg_app import config


class StockBase(SQLModel):
    symbol: str = Field(default=None, nullable=False)       # Basic Pydantic Validation
    country: str = Field(default=None, nullable=False)
    volume: int = Field(default=None, nullable=False, gt=0)
    dayprice: float = Field(default=None, nullable=False, gt=1)

async def get_test_stocks() -> [StockBase] :
    data_folder = config['data']['data_folder']
    print(f"Using Data Folder: {data_folder}")
    inp_File = f"{data_folder}/josn_test.dat"
    async with aiof.open(inp_File, "r") as inp:
        json_inp_str= await inp.read()
    print(f"Captured {inp_File}  Done:\n {json_inp_str}")

    #return json.loads(json_inp_str)['StockBase']
    return json.loads(json_inp_str)


async def old_get_test_stocks() -> [StockBase] :
    inp_json_file="C:/Users/Public/py_dev/fastapi/stock_sql/src/data/test_stocks.json"
    with open(inp_json_file, 'r') as f:
         test_stocks_from_file = json.load(f)['stocks']
    return(test_stocks_from_file)