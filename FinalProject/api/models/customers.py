from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from ..dependencies.database import Base

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    phone_number = Column(Integer, nullable=True, unique=True)
    address = Column(String(300), nullable=False)
    payment_info = Column(String(300))
