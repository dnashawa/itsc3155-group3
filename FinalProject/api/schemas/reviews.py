from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .customers import Customer

class ReviewBase(BaseModel):
    rating: int
    description: Optional[str] = None
    date: Optional[datetime]

class ReviewCreate(ReviewBase):
    customer_id: int

class ReviewUpdate(BaseModel):
    rating: Optional[int] = None
    description: Optional[str] = None
    date: Optional[datetime] = None
    customer_id: Optional[str] = None

class Review(ReviewBase):
    id: int
    customer: Customer = None

    class ConfigDict:
        from_attributes = True
