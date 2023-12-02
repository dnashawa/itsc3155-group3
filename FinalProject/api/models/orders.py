from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    description = Column(String(300))
    phone_number = Column(Integer, nullable=True, unique=True)
    address = Column(String(300), nullable=False)
    type = Column(String(100), nullable=False)
    status = Column(String(100), nullable=False)
    promo_code = Column(String, ForeignKey('promo_codes.code'), nullable=True)

    order_details = relationship("OrderDetail", back_populates="order")
    promo_codes = relationship("PromoCode", back_populates="order")