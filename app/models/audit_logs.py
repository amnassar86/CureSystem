from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)  # بدلاً من user_id
    action_type = Column(String(50), nullable=False)  # نوع الإجراء (إضافة، تعديل، حذف)
    table_name = Column(String(255), nullable=False)  # اسم الجدول
    record_id = Column(Integer, nullable=False)  # معرّف السجل
    old_data = Column(Text, nullable=True)  # البيانات القديمة
    new_data = Column(Text, nullable=True)  # البيانات الجديدة
    action_date = Column(DateTime, default=datetime.utcnow)
    ip_address = Column(String(45), nullable=True)
    device_info = Column(String(255), nullable=True)

    # العلاقة مع جدول الموظفين
    employee = relationship("Employee", back_populates="audit_logs")
