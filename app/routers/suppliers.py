from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.suppliers import Supplier as SupplierModel
from app.schemas.supplier_schemas import SupplierCreate, Supplier, SupplierUpdate

router = APIRouter()

# مسار لإضافة مورد جديد (POST)
@router.post("/", response_model=Supplier)
def create_supplier(supplier: SupplierCreate, db: Session = Depends(get_db)):
    db_supplier = SupplierModel(**supplier.dict())
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

@router.get("/", response_model=list[Supplier])
def read_suppliers(db: Session = Depends(get_db)):
    try:
        suppliers = db.query(SupplierModel).all()
        if not suppliers:
            raise HTTPException(status_code=404, detail="No suppliers found")
        return suppliers
    except Exception as e:
        print(f"Error occurred: {e}")  # طباعة الخطأ لمعرفة السبب الفعلي
        raise HTTPException(status_code=400, detail=f"Failed to fetch suppliers: {str(e)}")



# مسار للحصول على مورد معين بناءً على ID
@router.get("/{supplier_id}", response_model=Supplier)
def read_supplier(supplier_id: int, db: Session = Depends(get_db)):
    db_supplier = db.query(SupplierModel).filter(SupplierModel.id == supplier_id).first()
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier

# مسار لتحديث بيانات مورد بناءً على ID (PUT)
@router.put("/{supplier_id}", response_model=Supplier)
def update_supplier(supplier_id: int, supplier: SupplierUpdate, db: Session = Depends(get_db)):
    db_supplier = db.query(SupplierModel).filter(SupplierModel.id == supplier_id).first()
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")

    for key, value in supplier.dict().items():
        setattr(db_supplier, key, value)

    db.commit()
    db.refresh(db_supplier)
    return db_supplier

# مسار لحذف مورد بناءً على ID (DELETE)
@router.delete("/{supplier_id}", response_model=dict)
def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    db_supplier = db.query(SupplierModel).filter(SupplierModel.id == supplier_id).first()
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")

    db.delete(db_supplier)
    db.commit()
    return {"message": "Supplier deleted successfully"}
