from pydantic import BaseModel
from typing import Optional
from datetime import date

# نموذج أساسي للوصفة الطبية
class PrescriptionBase(BaseModel):
    patient_id: int
    prescription_date: date
    details: Optional[str] = None
    medication_id: int
    doctor_id: int

# نموذج لإنشاء وصفة طبية جديدة
class PrescriptionCreate(PrescriptionBase):
    pass

# نموذج لعرض بيانات الوصفة الطبية
class Prescription(PrescriptionBase):
    id: int

    class Config:
        from_attributes = True

# نموذج لتحديث بيانات الوصفة الطبية
class PrescriptionUpdate(BaseModel):
    patient_id: Optional[int] = None
    prescription_date: Optional[date] = None
    details: Optional[str] = None
    medication_id: Optional[int] = None
    doctor_id: Optional[int] = None
