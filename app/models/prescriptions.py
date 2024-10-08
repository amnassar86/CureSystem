from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Prescription(Base):
    __tablename__ = "prescriptions"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    prescription_date = Column(Date, nullable=False)
    details = Column(String, nullable=True)
    medication_id = Column(Integer, ForeignKey("medications.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("employees.id"), nullable=False)

    # العلاقات
    patient = relationship("Patient", back_populates="prescriptions")
    medication = relationship("Medication", back_populates="prescriptions")
    doctor = relationship("Employee", back_populates="prescriptions")
    sales = relationship("Sale", back_populates="prescription")
