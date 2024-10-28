#  see :  https://docs.sqlalchemy.org/en/20/tutorial/engine.html
## pool, sql verbose,  and asynch Future Support
class Db_Connect_URL:
    host:str="localhost"
    user:str="dev_user"
    passwd:str="dev_password"
    db_name:str="dev"
    port:int=5433
    pool_size:int = 2
    max_overflow:int = 3
    echo:bool  = True
# SQLALCHEMY_DATABASE_URL = "postgresql://dev_user:dev_password@localhost:5433/dev"
