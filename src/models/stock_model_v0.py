
from sqlmodel import Field, Session, SQLModel,select
class StockBase(SQLModel):
    symbol: str | None = None
    country: str | None = None
    volume: int | None = None
    dayprice: float | None = None



class Stock(StockBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


  # *********************** __repr__ for debug and print *********************

    def __repr__(self):
        return f"Stock:(symbol={self.symbol} , country = {self.country}, dayprice = {self.dayprice})"

  # *********************** __repr__ for debug and print *********************

####  New for Update to represents input for update DB
#####    https://sqlmodel.tiangolo.com/tutorial/fastapi/update/#heroupdate-model
class StockUpdate(SQLModel):
    symbol: str | None = None
    country: str | None = None
    volume: int | None = None
    dayprice: float | None = None