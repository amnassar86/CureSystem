from pydantic import BaseModel
from typing import Optional
from datetime import date

# نموذج أساسي للأدوية
class MedicationBase(BaseModel):
    name: str
    scientific_name: str
    dosage_form: Optional[str] = None
    price: float
    quantity: int
    expiration_date: date
    manufacturer: Optional[str] = None
    min_stock_level: Optional[int] = None
    requires_prescription: bool
    category: str
    discount: Optional[float] = 0.0
    category_id: Optional[int] = None
    barcode_international: Optional[str] = None
    barcode_local: Optional[str] = None
    description: Optional[str] = None
    side_effects: Optional[str] = None
    purchase_price: Optional[float] = None

# نموذج لإنشاء دواء جديد
class MedicationCreate(MedicationBase):
    pass

# نموذج لعرض بيانات الدواء
class Medication(MedicationBase):
    id: int

    class Config:
        from_attributes = True  # تم تحديث هذا بناءً على تحذيرات Pydantic

# نموذج لتحديث بيانات الدواء
class MedicationUpdate(BaseModel):
    name: Optional[str] = None
    scientific_name: Optional[str] = None
    dosage_form: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    expiration_date: Optional[date] = None
    manufacturer: Optional[str] = None
    min_stock_level: Optional[int] = None
    requires_prescription: Optional[bool] = None
    category: Optional[str] = None
    discount: Optional[float] = None
    category_id: Optional[int] = None
    barcode_international: Optional[str] = None
    barcode_local: Optional[str] = None
    description: Optional[str] = None
    side_effects: Optional[str] = None
    purchase_price: Optional[float] = None
