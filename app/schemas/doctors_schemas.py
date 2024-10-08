from pydantic import BaseModel

class DoctorBase(BaseModel):
    first_name: str
    last_name: str
    contact_info: str | None = None
    phone_number: str | None = None
    email: str | None = None
    clinic_name: str | None = None
    specialization: str | None = None  # العمود الجديد

class DoctorCreate(DoctorBase):
    pass

class Doctor(DoctorBase):
    id: int

    class Config:
        orm_mode = True
