from pydantic import BaseModel
from datetime import date, datetime

class ArchivedInvoiceBase(BaseModel):
    sale_id: int
    invoice_date: date
    total_amount: float
    invoice_discount: float | None = None
    invoice_type: str
    supplier_id: int | None = None
    customer_id: int | None = None
    employee_id: int | None = None

class ArchivedInvoiceCreate(ArchivedInvoiceBase):
    pass

class ArchivedInvoice(ArchivedInvoiceBase):
    id: int
    archived_at: datetime

    class Config:
        orm_mode = True
