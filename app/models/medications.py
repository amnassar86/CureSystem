from sqlalchemy import Column, Integer, String, Float, Boolean, Date
from app.database import Base
from sqlalchemy.orm import relationship

class Medication(Base):
    __tablename__ = "medications"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    scientific_name = Column(String, nullable=False)
    dosage_form = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    expiration_date = Column(Date, nullable=False)
    manufacturer = Column(String, nullable=True)
    min_stock_level = Column(Integer, nullable=True)
    requires_prescription = Column(Boolean, nullable=False)
    category = Column(String, nullable=False)
    discount = Column(Float, default=0.0)
    category_id = Column(Integer, nullable=True)
    barcode_international = Column(String, nullable=True)
    barcode_local = Column(String, nullable=True)
    description = Column(String, nullable=True)
    side_effects = Column(String, nullable=True)
    purchase_price = Column(Float, nullable=True)
    
        # إضافة العلاقة مع جدول prescriptions
    prescriptions = relationship("Prescription", back_populates="medication")
     # العلاقة مع notifications
    notifications = relationship("Notification", back_populates="medication")
