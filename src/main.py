###     https://fastapi.tiangolo.com/tutorial/sql-databases/#read-one-hero  Guide ####
## https://testdriven.io/blog/fastapi-sqlmodel/ to be applied
import os

import toml
import uvicorn
from fastapi import Depends, FastAPI,  Query
from sqlmodel import Field,  SQLModel,select

from .db.connect_cfg_db import  engine_cfg
from .routers.hero_routers import hero_router
from .routers.stock_routers import stock_router
from .test.stock_json_file_router import test_router_json



def create_db_and_tables():
    SQLModel.metadata.create_all(engine_cfg)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "FastApi SQLModel CRUD API"}

app.include_router(hero_router)
app.include_router(stock_router)
app.include_router(test_router_json)
#
# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()


# Not Working use command line as per next Note::
# def main():
#     if __name__ == "__main__":
#         uvicorn.run(app, host="localhost", port=8000)
#Run Notes ..........................................................
## run options fastapi or uvicorn
### 1- run fastapi from src::  fastapi dev main.py
''' Note:: ****************************************** uvicorn
### 2- Run uvicorn :
# from   test_SQLMode issue the next command 
uvicorn src.main:app --host localhost --port 800 --reload
uvicorn ************************************************ uvicorn '''
#Run Notes ..........................................................