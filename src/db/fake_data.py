import asyncio
import random
from faker import Faker

from src.models.stock_model import Stock,StockBase

symbols = ['AAPL', 'MSFT', 'GOOG', 'GOOGL', 'AMZN', 'TSLA', 'NVDA','PEP','COST','CSCO','QCOM']
fake = Faker()

async def db_rec(i:int):
    stock = StockBase()
    stock.symbol= f"{fake.random_element(symbols)}{i}"
    stock.country = fake.country()
    stock.dayprice= random.randrange(100, 200 )
    stock.volume = fake.random_number(8,True)

    return stock
async def get_list_of_stocks():
    lis_db=  [  await db_rec(i) for i in range(10)]
    print(len(lis_db))
    return lis_db
''' Test  '''
lis_out=  asyncio.run(get_list_of_stocks())
for stk in lis_out:
    print(stk.__repr__())
