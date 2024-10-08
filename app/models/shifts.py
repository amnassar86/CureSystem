from sqlalchemy import Column, Integer, String, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Shift(Base):
    __tablename__ = "shifts"
    
    id = Column(Integer, primary_key=True, index=True)
    shift_name = Column(String(255), nullable=True)
    start_time = Column(Time, nullable=True)
    end_time = Column(Time, nullable=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=True)

    # العلاقة مع جدول الموظفين
    employee = relationship("Employee", back_populates="shifts")
    
    cash_registers = relationship("CashRegister", back_populates="shift")
    transactions = relationship("Transaction", back_populates="shift")
