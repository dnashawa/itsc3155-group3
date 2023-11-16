from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ReviewBase(BaseModel):
    rating: int
    description: Optional[str] = None
    date: Optional[datetime]

class ReviewCreate(ReviewBase):
    pass

class ReviewUpdate(BaseModel):
    rating: Optional[int] = None
    description: Optional[str] = None
    date: Optional[datetime] = None

class Review(ReviewBase):
    id: int
    customer_id: int

    class ConfigDict:
        from_attributes = True
