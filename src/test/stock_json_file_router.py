from fastapi import HTTPException
from fastapi import APIRouter

from src.models.stock_model import StockBase
from src.test.read_stock_json import get_test_stocks

test_router_json = APIRouter()
@test_router_json.get('/select_stock_json/{test_stock_symb}', response_model=list[StockBase] ,status_code=200, tags=["stock_fromjson"])
async def get_stock(test_stock_symb: str) -> [StockBase]:
    print(f"input stock_symbol {test_stock_symb}")
    # old way nees some tuning stock_t = [t_stock for t_stock in await get_test_stocks() if t_stock['symbol'] == test_stock_symb]
    #StockBase
    lis_found= [ d for d in await get_test_stocks() if d['symbol'] == test_stock_symb]
    if len(lis_found) == 0:
        raise HTTPException(
            status_code=404, detail=f"No stock {test_stock_symb} found."
         )

    #return stock_t[0]
    return lis_found