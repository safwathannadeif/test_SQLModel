
from sqlmodel import Field, Session, SQLModel,select

class HeroBase(SQLModel):
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_name: str

    # *********************** __repr__ for debug and print *********************
    def __repr__(self):
        return f"HeroBase(name={self.name} age = {self.age}, secret_name = {self.secret_name})"
    # *********************** __repr__ for debug and print *********************

class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class HeroUpdate(HeroBase):
    name: str | None = None
    age: int | None = None
    secret_name: str | None = None

