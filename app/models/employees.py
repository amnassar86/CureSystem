from sqlalchemy import Column, Integer, String, Date
from app.database import Base
from sqlalchemy.orm import relationship

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role = Column(String)
    contact_info = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    email = Column(String, nullable=True)
    hire_date = Column(Date)
    status = Column(String, nullable=True)
    salary = Column(Integer)

    # إضافة العلاقة مع جدول sales
    sales = relationship("Sale", back_populates="pharmacist")
        # إضافة العلاقة مع جدول prescriptions
    prescriptions = relationship("Prescription", back_populates="doctor")
    shifts = relationship("Shift", back_populates="employee")
    user_roles = relationship("UserRole", back_populates="employee", primaryjoin="Employee.id == UserRole.employee_id")
        # العلاقة مع notifications
    notifications = relationship("Notification", back_populates="employee")
    
        # العلاقة مع جدول audit_logs
    audit_logs = relationship("AuditLog", back_populates="employee")
        # العلاقة مع archived_invoices
    archived_invoices = relationship("ArchivedInvoice", back_populates="employee")