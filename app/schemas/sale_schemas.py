from pydantic import BaseModel
from typing import Optional
from datetime import date, time

# نموذج أساسي لعملية البيع
class SaleBase(BaseModel):
    prescription_id: int
    sale_date: date
    total_amount: float
    tax_amount: float
    discount: Optional[float] = None
    payment_method: str
    customer_id: int
    pharmacist_id: int
    sale_time: time

# نموذج لإنشاء عملية بيع جديدة
class SaleCreate(SaleBase):
    pass

# نموذج لعرض بيانات عملية البيع
class Sale(SaleBase):
    id: int

    class Config:
        from_attributes = True

# نموذج لتحديث بيانات عملية البيع
class SaleUpdate(BaseModel):
    prescription_id: Optional[int] = None
    sale_date: Optional[date] = None
    total_amount: Optional[float] = None
    tax_amount: Optional[float] = None
    discount: Optional[float] = None
    payment_method: Optional[str] = None
    customer_id: Optional[int] = None
    pharmacist_id: Optional[int] = None
    sale_time: Optional[time] = None
