from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True)
    phone_number = Column(String(15), nullable=True)

    # إضافة العلاقة مع جدول sales
    sales = relationship("Sale", back_populates="customer")
        # إضافة العلاقة مع جدول invoices
    invoices = relationship("Invoice", back_populates="customer")
        # العلاقة مع archived_invoices
    archived_invoices = relationship("ArchivedInvoice", back_populates="customer")
