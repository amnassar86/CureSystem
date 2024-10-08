from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship

class Permission(Base):
    __tablename__ = "permissions"
    
    id = Column(Integer, primary_key=True, index=True)
    permission_name = Column(String(50), nullable=False, unique=True)  # اسم الصلاحية ويجب أن يكون فريدًا

    role_permissions = relationship("RolePermission", back_populates="permission")
