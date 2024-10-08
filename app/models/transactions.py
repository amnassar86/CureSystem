from sqlalchemy import Column, Integer, DECIMAL, Enum, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import enum

# تعريف نوع المعاملة كـ enum
class TransactionType(enum.Enum):
    addition = "addition"
    deduction = "deduction"

# تعريف وسيلة الدفع كـ enum
class PaymentMethod(enum.Enum):
    cash = "cash"
    card = "card"
    bank_transfer = "bank_transfer"

class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(DECIMAL(10, 2), nullable=False)
    transaction_type = Column(Enum(TransactionType), nullable=False)
    shift_id = Column(Integer, ForeignKey("shifts.id"), nullable=True)
    transaction_date = Column(DateTime, nullable=False)
    description = Column(String(255), nullable=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=True)
    payment_method = Column(Enum(PaymentMethod), default=PaymentMethod.cash, nullable=False)

    # العلاقات مع الجداول الأخرى
    shift = relationship("Shift", back_populates="transactions")
    invoice = relationship("Invoice", back_populates="transactions")
