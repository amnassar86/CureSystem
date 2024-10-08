from pydantic import BaseModel
from typing import Optional
from datetime import date

# القاعدة المشتركة لبيانات المريض
class PatientBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    gender: str
    contact_info: Optional[str] = None
    medical_history: Optional[str] = None

# نموذج لإنشاء مريض جديد
class PatientCreate(PatientBase):
    pass  # يمكن إضافة أي حقول إضافية إذا لزم الأمر

# نموذج لعرض بيانات المريض
class Patient(PatientBase):
    id: int

    class Config:
        orm_mode = True

# نموذج لتحديث بيانات المريض
class PatientUpdate(PatientBase):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    birth_date: Optional[date] = None
    gender: Optional[str] = None
    contact_info: Optional[str] = None
    medical_history: Optional[str] = None
