from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail


class PromoCodeBase(BaseModel):
    discount: int
    description: str
    end_date: datetime


class PromoCodeCreate(PromoCodeBase):
    pass


class PromoCodeUpdate(BaseModel):
    discount: Optional[int]
    description: Optional[str]
    end_date: Optional[datetime]


class PromoCode(PromoCodeBase):
    code: str
    start_date: Optional[datetime] = None

    class ConfigDict:
        from_attributes = True
