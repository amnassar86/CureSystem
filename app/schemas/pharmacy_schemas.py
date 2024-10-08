from pydantic import BaseModel
from typing import Optional

# نموذج أساسي للصيدلية
class PharmacyBase(BaseModel):
    name: str
    address: str
    phone_number: Optional[str] = None
    mobile_number: Optional[str] = None
    tax_registration_number: Optional[str] = None
    number_of_warehouses: Optional[int] = 1

# نموذج لإنشاء صيدلية جديدة
class PharmacyCreate(PharmacyBase):
    pass

# نموذج لعرض بيانات الصيدلية
class Pharmacy(PharmacyBase):
    id: int

    class Config:
        from_attributes = True

# نموذج لتحديث بيانات الصيدلية
class PharmacyUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    phone_number: Optional[str] = None
    mobile_number: Optional[str] = None
    tax_registration_number: Optional[str] = None
    number_of_warehouses: Optional[int] = 1
