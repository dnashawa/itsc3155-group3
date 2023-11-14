from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class SandwichBase(BaseModel):
    sandwich_name: str
    price: float
    calories: Optional[int]


class SandwichCreate(SandwichBase):
    pass


class SandwichUpdate(BaseModel):
    sandwich_name: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None


class Sandwich(SandwichBase):
    id: int

    class ConfigDict:
        from_attributes = True