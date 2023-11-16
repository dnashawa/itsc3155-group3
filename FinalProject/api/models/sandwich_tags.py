from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class SandwichTags(Base):
    __tablename__ = "sandwich_tags"

    sandwich_id = Column(Integer, ForeignKey('sandwiches.id'), primary_key=True)
    tags = Column(String(100), primary_key=True)

    sandwich = relationship("Sandwich", back_populates="sandwich_tags")

