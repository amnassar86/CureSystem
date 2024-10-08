from sqlalchemy import Column, Integer, Float, Date, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class ArchivedInvoice(Base):
    __tablename__ = "archived_invoices"

    id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, ForeignKey("sales.id"), nullable=False)
    invoice_date = Column(Date, nullable=False)
    total_amount = Column(Float, nullable=False)
    invoice_discount = Column(Float, nullable=True)
    invoice_type = Column(Enum('sale', 'purchase', 'refund'), nullable=False)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)
    archived_at = Column(DateTime, default=datetime.utcnow)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=True)

    # العلاقات
    sale = relationship("Sale")
    supplier = relationship("Supplier")
    customer = relationship("Customer")
    employee = relationship("Employee")
