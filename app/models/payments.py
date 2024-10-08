from sqlalchemy import Column, Integer, DECIMAL, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import enum

# تعريف حالة الدفع كـ enum
class PaymentStatus(enum.Enum):
    paid = "paid"
    partial = "partial"
    unpaid = "unpaid"

class Payment(Base):
    __tablename__ = "payments"
    
    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=False)
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    paid_amount = Column(DECIMAL(10, 2), nullable=False)
    remaining_amount = Column(DECIMAL(10, 2), nullable=False)
    payment_due_date = Column(Date, nullable=False)
    status = Column(Enum(PaymentStatus), default=PaymentStatus.unpaid, nullable=False)

    # العلاقة مع جدول الفواتير
    invoice = relationship("Invoice", back_populates="payments")
