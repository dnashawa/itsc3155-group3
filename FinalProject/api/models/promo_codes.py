from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class PromoCode(Base):
    __tablename__ = "promo_codes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(100), primary_key=True, index=True)
    discount = Column(DECIMAL)
    description = Column(String(300), nullable=False)
    start_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    end_date = Column(DATETIME, nullable=False)