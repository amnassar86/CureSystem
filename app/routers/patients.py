from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.patients import Patient as PatientModel
from app.schemas import PatientCreate, Patient, PatientUpdate  # إضافة PatientUpdate schema
from app.models.prescriptions import Prescription as PrescriptionModel  # تأكد من استيراد نموذج Prescription


router = APIRouter()

# مسار لإضافة مريض جديد
@router.post("/", response_model=Patient)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    db_patient = PatientModel(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

# مسار للحصول على مريض بناءً على ID
@router.get("/{patient_id}", response_model=Patient)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = db.query(PatientModel).filter(PatientModel.id == patient_id).first()
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

# مسار للحصول على جميع المرضى
@router.get("/", response_model=List[Patient])
def read_patients(db: Session = Depends(get_db)):
    return db.query(PatientModel).all()

# مسار لتحديث بيانات مريض بناءً على ID
@router.put("/{patient_id}", response_model=Patient)
def update_patient(patient_id: int, patient: PatientUpdate, db: Session = Depends(get_db)):
    db_patient = db.query(PatientModel).filter(PatientModel.id == patient_id).first()
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    # تحديث البيانات
    for key, value in patient.dict().items():
        setattr(db_patient, key, value)

    db.commit()
    db.refresh(db_patient)
    return db_patient

# مسار لحذف مريض بناءً على ID
@router.delete("/{patient_id}", response_model=dict)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    db_prescriptions = db.query(PrescriptionModel).filter(PrescriptionModel.patient_id == patient_id).all()
    for prescription in db_prescriptions:
        db.delete(prescription)
    
    db_patient = db.query(PatientModel).filter(PatientModel.id == patient_id).first()
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")

    db.delete(db_patient)
    db.commit()
    return {"message": "Patient and related prescriptions deleted successfully"}


