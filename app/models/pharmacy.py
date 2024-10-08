from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Pharmacy(Base):
    __tablename__ = "pharmacy"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    address = Column(Text, nullable=False)
    phone_number = Column(String(15), nullable=True)
    mobile_number = Column(String(15), nullable=True)
    tax_registration_number = Column(String(50), nullable=True)
    number_of_warehouses = Column(Integer, nullable=True, default=1)
