from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.cash_register import CashRegister as CashRegisterModel
from app.schemas.cash_register_schemas import CashRegisterCreate, CashRegister, CashRegisterUpdate

router = APIRouter()

# مسار لإضافة سجل نقدية جديد (POST)
@router.post("/", response_model=CashRegister)
def create_cash_register(cash_register: CashRegisterCreate, db: Session = Depends(get_db)):
    try:
        db_cash_register = CashRegisterModel(**cash_register.dict())
        db.add(db_cash_register)
        db.commit()
        db.refresh(db_cash_register)
        return db_cash_register
    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=400, detail="Failed to create cash register")

# مسار للحصول على جميع سجلات النقدية (GET)
@router.get("/", response_model=list[CashRegister])
def read_cash_registers(db: Session = Depends(get_db)):
    try:
        cash_registers = db.query(CashRegisterModel).all()
        return cash_registers
    except Exception as e:
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=400, detail="Failed to fetch cash registers")

# مسار للحصول على سجل نقدية معين بناءً على ID (GET by ID)
@router.get("/{cash_register_id}", response_model=CashRegister)
def read_cash_register(cash_register_id: int, db: Session = Depends(get_db)):
    db_cash_register = db.query(CashRegisterModel).filter(CashRegisterModel.id == cash_register_id).first()
    if db_cash_register is None:
        raise HTTPException(status_code=404, detail="Cash Register not found")
    return db_cash_register

# مسار لتحديث سجل نقدية بناءً على ID (PUT)
@router.put("/{cash_register_id}", response_model=CashRegister)
def update_cash_register(cash_register_id: int, cash_register: CashRegisterUpdate, db: Session = Depends(get_db)):
    db_cash_register = db.query(CashRegisterModel).filter(CashRegisterModel.id == cash_register_id).first()
    if db_cash_register is None:
        raise HTTPException(status_code=404, detail="Cash Register not found")

    # تحديث البيانات فقط إذا كانت موجودة في الطلب
    update_data = cash_register.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_cash_register, key, value)

    db.commit()
    db.refresh(db_cash_register)
    return db_cash_register


# مسار لحذف سجل نقدية بناءً على ID (DELETE)
@router.delete("/{cash_register_id}", response_model=dict)
def delete_cash_register(cash_register_id: int, db: Session = Depends(get_db)):
    db_cash_register = db.query(CashRegisterModel).filter(CashRegisterModel.id == cash_register_id).first()
    if db_cash_register is None:
        raise HTTPException(status_code=404, detail="Cash Register not found")

    db.delete(db_cash_register)
    db.commit()
    return {"message": "Cash Register deleted successfully"}
