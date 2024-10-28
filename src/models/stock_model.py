
from sqlmodel import Field, Session, SQLModel,select
class StockBase(SQLModel):
    symbol: str = Field(default=None, nullable=False)       # Basic Pydantic Validation
    country: str = Field(default=None, nullable=False)
    volume: int = Field(default=None, nullable=False, gt=0)
    dayprice: float = Field(default=None, nullable=False, gt=1)

class Stock(StockBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)


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