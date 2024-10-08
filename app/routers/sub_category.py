from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.sub_category import SubCategory as SubCategoryModel
from app.schemas.sub_category_schemas import SubCategoryCreate, SubCategory

router = APIRouter()

# مسار لإضافة تصنيف فرعي جديد (POST)
@router.post("/", response_model=SubCategory)
def create_sub_category(sub_category: SubCategoryCreate, db: Session = Depends(get_db)):
    db_sub_category = SubCategoryModel(**sub_category.dict())
    db.add(db_sub_category)
    db.commit()
    db.refresh(db_sub_category)
    return db_sub_category

# مسار للحصول على جميع التصنيفات الفرعية (GET)
@router.get("/", response_model=list[SubCategory])
def read_sub_categories(db: Session = Depends(get_db)):
    return db.query(SubCategoryModel).all()

# مسار للحصول على تصنيف فرعي معين بناءً على ID (GET by ID)
@router.get("/{sub_category_id}", response_model=SubCategory)
def read_sub_category(sub_category_id: int, db: Session = Depends(get_db)):
    db_sub_category = db.query(SubCategoryModel).filter(SubCategoryModel.id == sub_category_id).first()
    if db_sub_category is None:
        raise HTTPException(status_code=404, detail="SubCategory not found")
    return db_sub_category

# مسار لتحديث تصنيف فرعي بناءً على ID (PUT)
@router.put("/{sub_category_id}", response_model=SubCategory)
def update_sub_category(sub_category_id: int, sub_category: SubCategoryCreate, db: Session = Depends(get_db)):
    db_sub_category = db.query(SubCategoryModel).filter(SubCategoryModel.id == sub_category_id).first()
    if db_sub_category is None:
        raise HTTPException(status_code=404, detail="SubCategory not found")

    for key, value in sub_category.dict().items():
        setattr(db_sub_category, key, value)

    db.commit()
    db.refresh(db_sub_category)
    return db_sub_category

# مسار لحذف تصنيف فرعي بناءً على ID (DELETE)
@router.delete("/{sub_category_id}", response_model=dict)
def delete_sub_category(sub_category_id: int, db: Session = Depends(get_db)):
    db_sub_category = db.query(SubCategoryModel).filter(SubCategoryModel.id == sub_category_id).first()
    if db_sub_category is None:
        raise HTTPException(status_code=404, detail="SubCategory not found")

    db.delete(db_sub_category)
    db.commit()
    return {"message": "SubCategory deleted successfully"}
