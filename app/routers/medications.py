from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.medications import Medication as MedicationModel
from app.schemas.medication_schemas import MedicationCreate, Medication, MedicationUpdate

router = APIRouter()

# مسار لإضافة دواء جديد (POST)
@router.post("/", response_model=Medication)
def create_medication(medication: MedicationCreate, db: Session = Depends(get_db)):
    db_medication = MedicationModel(**medication.dict())
    db.add(db_medication)
    db.commit()
    db.refresh(db_medication)
    return db_medication

# مسار للحصول على جميع الأدوية (GET)
@router.get("/", response_model=list[Medication])
def read_medications(db: Session = Depends(get_db)):
    return db.query(MedicationModel).all()

# مسار للحصول على دواء معين بناءً على ID
@router.get("/{medication_id}", response_model=Medication)
def read_medication(medication_id: int, db: Session = Depends(get_db)):
    db_medication = db.query(MedicationModel).filter(MedicationModel.id == medication_id).first()
    if db_medication is None:
        raise HTTPException(status_code=404, detail="Medication not found")
    return db_medication

# مسار لتحديث دواء بناءً على ID (PUT)
@router.put("/{medication_id}", response_model=Medication)
def update_medication(medication_id: int, medication: MedicationUpdate, db: Session = Depends(get_db)):
    db_medication = db.query(MedicationModel).filter(MedicationModel.id == medication_id).first()
    if db_medication is None:
        raise HTTPException(status_code=404, detail="Medication not found")

    for key, value in medication.dict().items():
        setattr(db_medication, key, value)

    db.commit()
    db.refresh(db_medication)
    return db_medication

# مسار لحذف دواء بناءً على ID (DELETE)
@router.delete("/{medication_id}", response_model=dict)
def delete_medication(medication_id: int, db: Session = Depends(get_db)):
    db_medication = db.query(MedicationModel).filter(MedicationModel.id == medication_id).first()
    if db_medication is None:
        raise HTTPException(status_code=404, detail="Medication not found")

    db.delete(db_medication)
    db.commit()
    return {"message": "Medication deleted successfully"}
