from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.shifts import Shift as ShiftModel
from app.schemas.shift_schemas import ShiftCreate, Shift, ShiftUpdate

router = APIRouter()

# مسار لإضافة وردية جديدة (POST)
@router.post("/", response_model=Shift)
def create_shift(shift: ShiftCreate, db: Session = Depends(get_db)):
    try:
        db_shift = ShiftModel(**shift.dict())
        db.add(db_shift)
        db.commit()
        db.refresh(db_shift)
        return db_shift
    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=400, detail="Failed to create shift")

# مسار للحصول على جميع الورديات (GET)
@router.get("/", response_model=list[Shift])
def read_shifts(db: Session = Depends(get_db)):
    try:
        shifts = db.query(ShiftModel).all()
        return shifts
    except Exception as e:
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=400, detail="Failed to fetch shifts")

# مسار للحصول على وردية معينة بناءً على ID (GET by ID)
@router.get("/{shift_id}", response_model=Shift)
def read_shift(shift_id: int, db: Session = Depends(get_db)):
    db_shift = db.query(ShiftModel).filter(ShiftModel.id == shift_id).first()
    if db_shift is None:
        raise HTTPException(status_code=404, detail="Shift not found")
    return db_shift

# مسار لتحديث وردية بناءً على ID (PUT)
@router.put("/{shift_id}", response_model=Shift)
def update_shift(shift_id: int, shift: ShiftUpdate, db: Session = Depends(get_db)):
    db_shift = db.query(ShiftModel).filter(ShiftModel.id == shift_id).first()
    if db_shift is None:
        raise HTTPException(status_code=404, detail="Shift not found")

    for key, value in shift.dict().items():
        if value is not None:
            setattr(db_shift, key, value)

    db.commit()
    db.refresh(db_shift)
    return db_shift

# مسار لحذف وردية بناءً على ID (DELETE)
@router.delete("/{shift_id}", response_model=dict)
def delete_shift(shift_id: int, db: Session = Depends(get_db)):
    db_shift = db.query(ShiftModel).filter(ShiftModel.id == shift_id).first()
    if db_shift is None:
        raise HTTPException(status_code=404, detail="Shift not found")

    db.delete(db_shift)
    db.commit()
    return {"message": "Shift deleted successfully"}
