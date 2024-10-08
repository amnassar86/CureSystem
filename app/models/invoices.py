from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.customers import Customer

class Invoice(Base):
    __tablename__ = "invoices"
    __table_args__ = {'extend_existing': True}  # حل مشكلة التكرار

    id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, nullable=False)
    invoice_date = Column(Date, nullable=False)
    total_amount = Column(Float, nullable=False)
    invoice_discount = Column(Float, nullable=True)
    invoice_type = Column(String, nullable=False)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)

    # العلاقات مع الجداول الأخرى
    supplier = relationship("Supplier", back_populates="invoices")
    customer = relationship("Customer", back_populates="invoices")
    payments = relationship("Payment", back_populates="invoice")
    transactions = relationship("Transaction", back_populates="invoice")
