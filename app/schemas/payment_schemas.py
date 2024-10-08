from pydantic import BaseModel
from typing import Optional
from datetime import date
from decimal import Decimal
from enum import Enum

# تعريف حالة الدفع كـ enum
class PaymentStatus(str, Enum):
    paid = "paid"
    partial = "partial"
    unpaid = "unpaid"

# نموذج أساسي للدفع
class PaymentBase(BaseModel):
    invoice_id: int
    total_amount: Decimal
    paid_amount: Decimal
    remaining_amount: Decimal
    payment_due_date: date
    status: PaymentStatus = PaymentStatus.unpaid

# نموذج لإنشاء دفع جديد
class PaymentCreate(PaymentBase):
    pass

# نموذج لعرض بيانات الدفع
class Payment(PaymentBase):
    id: int

    class Config:
        from_attributes = True

# نموذج لتحديث بيانات الدفع
class PaymentUpdate(BaseModel):
    total_amount: Optional[Decimal] = None
    paid_amount: Optional[Decimal] = None
    remaining_amount: Optional[Decimal] = None
    payment_due_date: Optional[date] = None
    status: Optional[PaymentStatus] = None
