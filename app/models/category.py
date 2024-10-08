from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Category(Base):
    __tablename__ = "category"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

    # العلاقة مع sub_category
    sub_categories = relationship("SubCategory", back_populates="category")
