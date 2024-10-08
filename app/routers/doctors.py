from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.doctors import Doctor as DoctorModel
from app.schemas.doctors_schemas import DoctorCreate, Doctor

router = APIRouter()

# مسار لإضافة طبيب جديد (POST)
@router.post("/", response_model=Doctor)
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    db_doctor = DoctorModel(**doctor.dict())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

# مسار للحصول على جميع الأطباء (GET)
@router.get("/", response_model=list[Doctor])
def read_doctors(db: Session = Depends(get_db)):
    return db.query(DoctorModel).all()

# مسار للحصول على طبيب معين بناءً على ID (GET by ID)
@router.get("/{doctor_id}", response_model=Doctor)
def read_doctor(doctor_id: int, db: Session = Depends(get_db)):
    db_doctor = db.query(DoctorModel).filter(DoctorModel.id == doctor_id).first()
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return db_doctor

# مسار لتحديث طبيب بناءً على ID (PUT)
@router.put("/{doctor_id}", response_model=Doctor)
def update_doctor(doctor_id: int, doctor: DoctorCreate, db: Session = Depends(get_db)):
    db_doctor = db.query(DoctorModel).filter(DoctorModel.id == doctor_id).first()
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")

    for key, value in doctor.dict().items():
        setattr(db_doctor, key, value)

    db.commit()
    db.refresh(db_doctor)
    return db_doctor

# مسار لحذف طبيب بناءً على ID (DELETE)
@router.delete("/{doctor_id}", response_model=dict)
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    db_doctor = db.query(DoctorModel).filter(DoctorModel.id == doctor_id).first()
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")

    db.delete(db_doctor)
    db.commit()
    return {"message": "Doctor deleted successfully"}
