from pydantic import BaseModel
from typing import Optional
from datetime import date

# نموذج لإنشاء فاتورة جديدة
class InvoiceCreate(BaseModel):
    sale_id: int
    invoice_date: date
    total_amount: float
    invoice_discount: Optional[float] = None
    invoice_type: str
    supplier_id: Optional[int] = None
    customer_id: Optional[int] = None

# نموذج لعرض بيانات الفاتورة
class Invoice(InvoiceCreate):
    id: int

    class Config:
        from_attributes = True
