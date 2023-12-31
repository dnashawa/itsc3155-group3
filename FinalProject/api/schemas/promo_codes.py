from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PromoCodeBase(BaseModel):
    code: str
    discount: float
    description: str
    end_date: datetime


class PromoCodeCreate(PromoCodeBase):
    pass


class PromoCodeUpdate(BaseModel):
    code: Optional[str]
    discount: Optional[float]
    description: Optional[str]
    end_date: Optional[datetime]


class PromoCode(PromoCodeBase):
    id: int
    #code: str
    start_date: Optional[datetime] = None

    class ConfigDict:
        from_attributes = True
