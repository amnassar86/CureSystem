from sqlalchemy import Column, Integer, DECIMAL, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class CashRegister(Base):
    __tablename__ = "cash_register"
    
    id = Column(Integer, primary_key=True, index=True)
    opening_balance = Column(DECIMAL(10, 2), nullable=False)
    closing_balance = Column(DECIMAL(10, 2), nullable=True)
    shift_id = Column(Integer, ForeignKey("shifts.id"), nullable=True)
    register_date = Column(Date, nullable=False)

    # العلاقة مع جدول الورديات
    shift = relationship("Shift", back_populates="cash_registers")
