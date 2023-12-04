from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail


class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None
    phone_number: Optional[str]
    address: str
    order_type: str
    order_status: str = "Not Started"
    promo_code_id: Optional[int]
    payment_type: str #lines 15 - 17 added by abby 12/2 to meet requirements
    payment_status: str = "Processing..."
    payment_info: Optional[str]


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None
    phone_number: Optional[str] #changed to string
    address: Optional[str]
    order_type: Optional[str]
    order_status: Optional[str] = "In Progress"
    promo_code_id: Optional[int]
    payment_type: Optional[str] #lines 33 - 35 added by abby 12/2 to meet requirements
    payment_status: Optional[str] = "Processed"
    payment_info: Optional[str]


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True
