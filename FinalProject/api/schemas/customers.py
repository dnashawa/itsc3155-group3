from typing import Optional
from pydantic import BaseModel


class CustomerBase(BaseModel):
    customer_name: str
    phone_number: Optional[int]
    address: str
    payment_info: str


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    customer_name: Optional[str] = None
    phone_number: Optional[int]
    address: Optional[str]
    payment_info: Optional[str]


class Customer(CustomerBase):
    id: int

    class ConfigDict:
        from_attributes = True