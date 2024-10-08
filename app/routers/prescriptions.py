from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.prescriptions import Prescription as PrescriptionModel
from app.schemas.prescription_schemas import PrescriptionCreate, Prescription, PrescriptionUpdate

router = APIRouter()

# مسار لإضافة وصفة طبية جديدة (POST)
@router.post("/", response_model=Prescription)
def create_prescription(prescription: PrescriptionCreate, db: Session = Depends(get_db)):
    db_prescription = PrescriptionModel(**prescription.dict())
    db.add(db_prescription)
    db.commit()
    db.refresh(db_prescription)
    return db_prescription

# مسار للحصول على جميع الوصفات الطبية (GET)
@router.get("/", response_model=list[Prescription])
def read_prescriptions(db: Session = Depends(get_db)):
    return db.query(PrescriptionModel).all()

# مسار للحصول على وصفة طبية معينة بناءً على ID
@router.get("/{prescription_id}", response_model=Prescription)
def read_prescription(prescription_id: int, db: Session = Depends(get_db)):
    db_prescription = db.query(PrescriptionModel).filter(PrescriptionModel.id == prescription_id).first()
    if db_prescription is None:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return db_prescription

# مسار لتحديث وصفة طبية بناءً على ID (PUT)
@router.put("/{prescription_id}", response_model=Prescription)
def update_prescription(prescription_id: int, prescription: PrescriptionUpdate, db: Session = Depends(get_db)):
    db_prescription = db.query(PrescriptionModel).filter(PrescriptionModel.id == prescription_id).first()
    if db_prescription is None:
        raise HTTPException(status_code=404, detail="Prescription not found")

    for key, value in prescription.dict().items():
        setattr(db_prescription, key, value)

    db.commit()
    db.refresh(db_prescription)
    return db_prescription

# مسار لحذف وصفة طبية بناءً على ID (DELETE)
@router.delete("/{prescription_id}", response_model=dict)
def delete_prescription(prescription_id: int, db: Session = Depends(get_db)):
    db_prescription = db.query(PrescriptionModel).filter(PrescriptionModel.id == prescription_id).first()
    if db_prescription is None:
        raise HTTPException(status_code=404, detail="Prescription not found")

    db.delete(db_prescription)
    db.commit()
    return {"message": "Prescription deleted successfully"}
