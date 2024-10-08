from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
from sqlalchemy.dialects.mysql import TINYINT

class Notification(Base):
    __tablename__ = "notifications"
    
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String(255), nullable=False)
    notification_type = Column(String(255), nullable=False)  # يمكن أن يكون انتهاء صلاحية أو غيره
    medication_id = Column(Integer, ForeignKey("medications.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_read = Column(Boolean, default=False)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=True)  # مرتبط بجدول employees
    priority = Column(Enum('low', 'medium', 'high'), default='medium')
    target_type = Column(Enum('admin', 'pharmacist', 'sales'), default='pharmacist')

    # العلاقات
    employee = relationship("Employee", back_populates="notifications")
    medication = relationship("Medication", back_populates="notifications")
