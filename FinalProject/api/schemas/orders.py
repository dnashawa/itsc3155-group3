from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail


class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None
    phone_number: Optional[str]
    address: str
    type: str
    status: str = "Not Started"
    promo_code_id: Optional[int]


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None
    phone_number: Optional[str] #changed to string
    address: Optional[str]
    type: Optional[str]
    status: Optional[str] = "In Progress"
    promo_code_id: Optional[int]


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True
