from pydantic import BaseModel
from typing import Optional

# نموذج أساسي للمورد
class SupplierBase(BaseModel):
    supplier_name: str
    tax_registration_number: str
    phone_number: Optional[str] = None

# نموذج لإنشاء مورد جديد
class SupplierCreate(BaseModel):
    supplier_name: str
    tax_registration_number: str
    phone_number: Optional[str] = None

# نموذج لعرض بيانات المورد
class Supplier(SupplierCreate):
    id: int

    class Config:
        from_attributes = True

# نموذج لتحديث بيانات المورد
class SupplierUpdate(BaseModel):
    supplier_name: Optional[str] = None
    tax_registration_number: Optional[str] = None
    phone_number: Optional[str] = None
