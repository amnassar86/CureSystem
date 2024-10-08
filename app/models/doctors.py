from sqlalchemy import Column, Integer, String
from app.database import Base

class Doctor(Base):
    __tablename__ = "doctors"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    contact_info = Column(String(255), nullable=True)
    phone_number = Column(String(15), nullable=True)
    email = Column(String(255), nullable=True)
    clinic_name = Column(String(255), nullable=True)
    specialization = Column(String(255), nullable=True)  # العمود الجديد للتخصص
