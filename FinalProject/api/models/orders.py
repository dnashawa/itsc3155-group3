from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, func
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    order_date = Column(DATETIME, nullable=False,
                        server_default=func.now())  # altered 12/4 by Dylan
    description = Column(String(300))
    phone_number = Column(String(20), nullable=True, unique=True) #changed to string since INT was not cooperating
    address = Column(String(300), nullable=False)
    order_type = Column(String(100), nullable=False)
    order_status = Column(String(100), nullable=False)
    promo_code_id = Column(Integer, ForeignKey('promo_codes.id'), nullable=True) #changed to promo_code_id since we added id to promo codes
    payment_type = Column(String(100), nullable=False) #lines 19 - 21 added by abby 12/2 to meet requirements
    payment_status = Column(String(100), nullable=False)
    payment_info = Column(String(300), nullable=True)
    order_details = relationship("OrderDetail", back_populates="order")
    promo_codes = relationship("PromoCode", back_populates="order")