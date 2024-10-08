from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class UserRole(Base):
    __tablename__ = "user_roles"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)

    # العلاقة مع جدول الموظفين
    employee = relationship("Employee", back_populates="user_roles", primaryjoin="UserRole.employee_id == Employee.id")

    # العلاقة مع جدول الأدوار
    role = relationship("Role", back_populates="user_roles", primaryjoin="UserRole.role_id == Role.id")
