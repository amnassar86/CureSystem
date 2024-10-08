from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.pharmacy import Pharmacy as PharmacyModel
from app.schemas.pharmacy_schemas import PharmacyCreate, Pharmacy, PharmacyUpdate

router = APIRouter()

# مسار لإضافة صيدلية جديدة (POST)
@router.post("/", response_model=Pharmacy)
def create_pharmacy(pharmacy: PharmacyCreate, db: Session = Depends(get_db)):
    try:
        db_pharmacy = PharmacyModel(**pharmacy.dict())
        db.add(db_pharmacy)
        db.commit()
        db.refresh(db_pharmacy)
        return db_pharmacy
    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=400, detail="Failed to create pharmacy")

# مسار للحصول على جميع الصيدليات (GET)
@router.get("/", response_model=list[Pharmacy])
def read_pharmacies(db: Session = Depends(get_db)):
    try:
        pharmacies = db.query(PharmacyModel).all()
        return pharmacies
    except Exception as e:
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=400, detail="Failed to fetch pharmacies")

# مسار للحصول على صيدلية معينة بناءً على ID (GET by ID)
@router.get("/{pharmacy_id}", response_model=Pharmacy)
def read_pharmacy(pharmacy_id: int, db: Session = Depends(get_db)):
    db_pharmacy = db.query(PharmacyModel).filter(PharmacyModel.id == pharmacy_id).first()
    if db_pharmacy is None:
        raise HTTPException(status_code=404, detail="Pharmacy not found")
    return db_pharmacy

# مسار لتحديث صيدلية بناءً على ID (PUT)
@router.put("/{pharmacy_id}", response_model=Pharmacy)
def update_pharmacy(pharmacy_id: int, pharmacy: PharmacyUpdate, db: Session = Depends(get_db)):
    db_pharmacy = db.query(PharmacyModel).filter(PharmacyModel.id == pharmacy_id).first()
    if db_pharmacy is None:
        raise HTTPException(status_code=404, detail="Pharmacy not found")

    for key, value in pharmacy.dict().items():
        if value is not None:
            setattr(db_pharmacy, key, value)

    db.commit()
    db.refresh(db_pharmacy)
    return db_pharmacy

# مسار لحذف صيدلية بناءً على ID (DELETE)
@router.delete("/{pharmacy_id}", response_model=dict)
def delete_pharmacy(pharmacy_id: int, db: Session = Depends(get_db)):
    db_pharmacy = db.query(PharmacyModel).filter(PharmacyModel.id == pharmacy_id).first()
    if db_pharmacy is None:
        raise HTTPException(status_code=404, detail="Pharmacy not found")

    db.delete(db_pharmacy)
    db.commit()
    return {"message": "Pharmacy deleted successfully"}
