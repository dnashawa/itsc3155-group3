from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich


class OrderDetailBase(BaseModel):
    amount: int


class OrderDetailCreate(OrderDetailBase):
    order_id: int
    sandwich_id: int


class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    sandwich_id: Optional[int] = None
    amount: Optional[int] = None
    review_description: Optional[str] = None
    rating: Optional[int] = None


class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    sandwich: Sandwich = None
    review_description: Optional[str] = None  # implemented December 1 by Dylan
    rating: Optional[int] = None    # implemented December 1 by Dylan

    class ConfigDict:
        from_attributes = True
