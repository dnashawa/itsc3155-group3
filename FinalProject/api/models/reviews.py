from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Reviews(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    rating = Column(Integer, nullable=False)
    description = Column(String(300), nullable=False)
    date = Column(DATETIME, server_default=str(datetime.now()), nullable=False)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)

    # Define the relationship with the Customer model
    customer = relationship("Customer", back_populates="reviews")
