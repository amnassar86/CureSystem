from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class SubCategory(Base):
    __tablename__ = "sub_category"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)

    # العلاقة مع جدول category
    category = relationship("Category", back_populates="sub_categories")
