from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class PromoCodes(Base):
    __tablename__ = "promo_codes"

    code = Column(String(100), primary_key=True, index=True)
    discount = Column(Integer) #figure out what data type discount should be
    description = Column(String(300), nullable=False)
    start_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    end_date = Column(DATETIME, nullable=False)
