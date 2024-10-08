from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey, Time
from sqlalchemy.orm import relationship
from app.database import Base

class Sale(Base):
    __tablename__ = "sales"
    
    id = Column(Integer, primary_key=True, index=True)
    prescription_id = Column(Integer, ForeignKey("prescriptions.id"), nullable=False)
    sale_date = Column(Date, nullable=False)
    total_amount = Column(Float, nullable=False)
    tax_amount = Column(Float, nullable=False)
    discount = Column(Float, nullable=True)
    payment_method = Column(String, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    pharmacist_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    sale_time = Column(Time, nullable=False)

    # العلاقات
    prescription = relationship("Prescription", back_populates="sales")
    customer = relationship("Customer", back_populates="sales")
    pharmacist = relationship("Employee", back_populates="sales")
        # العلاقة مع archived_invoices
    archived_invoices = relationship("ArchivedInvoice", back_populates="sale")
