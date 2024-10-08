from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Supplier(Base):
    __tablename__ = "suppliers"
    
    id = Column(Integer, primary_key=True, index=True)
    supplier_name = Column(String, nullable=False)
    tax_registration_number = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)

    # العلاقة مع جدول invoices
    invoices = relationship("Invoice", back_populates="supplier")
