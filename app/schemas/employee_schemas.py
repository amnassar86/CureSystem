from pydantic import BaseModel
from typing import Optional
from datetime import date

# نموذج لإنشاء موظف جديد
class EmployeeCreate(BaseModel):
    name: str
    role: str
    contact_info: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    hire_date: date
    status: Optional[str] = None
    salary: int

# نموذج لعرض بيانات الموظف
class Employee(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True

# نموذج لتحديث بيانات الموظف
class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    contact_info: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    hire_date: Optional[date] = None
    status: Optional[str] = None
    salary: Optional[int] = None
