from typing import Annotated

from fastapi import Depends
from sqlmodel import  create_engine
from sqlmodel import Session
from ..cfg.db_config import Db_Connect_URL


con_cfg = Db_Connect_URL()
pool_size_cfg=con_cfg.pool_size
max_overflow_cfg=con_cfg.max_overflow
echo_cfg=con_cfg.echo
engine_cfg=None


def get_db_url() -> str:
    ret_url = f"postgresql://{con_cfg.user}:{con_cfg.passwd}@{con_cfg.host}:{con_cfg.port}/{con_cfg.db_name}"
    return ret_url

engine_cfg = create_engine(get_db_url(), pool_size=con_cfg.pool_size, max_overflow=con_cfg.max_overflow, echo=con_cfg.echo)


# SQLALCHEMY_DATABASE_URL = "postgresql://dev_user:dev_password@localhost:5433/dev"
# connect_args = {"check_same_thread": False}

def get_session():
    with Session(engine_cfg) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

'''  
Before SQLModel 
#Base = declarative_base()
# we should use https://fastapi.tiangolo.com/tutorial/sql-databases/#create-a-hero
#Yield DB Sessions from SQLALCHEMY pool
# def get_session_db():
#     try:
#         db_session = SessionLocal()
#         yield db_session
#     finally:
#         db_session.close()
'''''
