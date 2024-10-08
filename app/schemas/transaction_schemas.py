from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal
from enum import Enum

# تعريف نوع المعاملة كـ enum
class TransactionType(str, Enum):
    addition = "addition"
    deduction = "deduction"

# تعريف وسيلة الدفع كـ enum
class PaymentMethod(str, Enum):
    cash = "cash"
    card = "card"
    bank_transfer = "bank_transfer"

# نموذج أساسي للمعاملة
class TransactionBase(BaseModel):
    amount: Decimal
    transaction_type: TransactionType
    shift_id: Optional[int] = None
    transaction_date: datetime
    description: Optional[str] = None
    invoice_id: Optional[int] = None
    payment_method: PaymentMethod = PaymentMethod.cash

# نموذج لإنشاء معاملة جديدة
class TransactionCreate(TransactionBase):
    pass

# نموذج لعرض بيانات المعاملة
class Transaction(TransactionBase):
    id: int

    class Config:
        from_attributes = True

# نموذج لتحديث بيانات المعاملة
class TransactionUpdate(BaseModel):
    amount: Optional[Decimal] = None
    transaction_type: Optional[TransactionType] = None
    shift_id: Optional[int] = None
    transaction_date: Optional[datetime] = None
    description: Optional[str] = None
    invoice_id: Optional[int] = None
    payment_method: Optional[PaymentMethod] = None
