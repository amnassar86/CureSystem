# app/models/patients.py
from sqlalchemy import Column, Integer, String, Date
from app.database import Base
from sqlalchemy.orm import relationship


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    birth_date = Column(Date)
    gender = Column(String(10))
    contact_info = Column(String(255))
    purchase_history = Column(String(255))
    medical_history = Column(String, nullable=True)  # تأكد من إضافة هذا الحقل
    
        # إضافة العلاقة مع جدول prescriptions
    prescriptions = relationship("Prescription", back_populates="patient")
