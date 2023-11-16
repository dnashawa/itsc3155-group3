from typing import Optional
from pydantic import BaseModel

class SandwichTagBase(BaseModel):
    tags: str

class SandwichTagCreate(SandwichTagBase):
    sandwich_id: int
    tags: str

class SandwichTagUpdate(BaseModel):
    sandwich_id: Optional[int] = None
    tags: Optional[str] = None

class SandwichTag(SandwichTagBase):
    pass

    class ConfigDict:
        from_attributes = True
