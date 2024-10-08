from pydantic import BaseModel
from typing import Optional
from datetime import date
from decimal import Decimal

# نموذج أساسي لسجل النقدية
class CashRegisterBase(BaseModel):
    opening_balance: Decimal
    closing_balance: Optional[Decimal] = None
    shift_id: Optional[int] = None
    register_date: date

# نموذج لإنشاء سجل نقدية جديد
class CashRegisterCreate(CashRegisterBase):
    pass

# نموذج لعرض بيانات سجل النقدية
class CashRegister(CashRegisterBase):
    id: int

    class Config:
        from_attributes = True

# نموذج لتحديث بيانات سجل النقدية
class CashRegisterUpdate(BaseModel):
    opening_balance: Optional[Decimal] = None
    closing_balance: Optional[Decimal] = None
    shift_id: Optional[int] = None
    register_date: Optional[date] = None
