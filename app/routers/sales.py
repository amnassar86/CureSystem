from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.sales import Sale as SaleModel
from app.schemas.sale_schemas import SaleCreate, Sale, SaleUpdate

router = APIRouter()

# مسار لإضافة عملية بيع جديدة (POST)
@router.post("/", response_model=Sale)
def create_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    db_sale = SaleModel(**sale.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

# مسار للحصول على جميع عمليات البيع (GET)
@router.get("/", response_model=list[Sale])
def read_sales(db: Session = Depends(get_db)):
    return db.query(SaleModel).all()

# مسار للحصول على عملية بيع معينة بناءً على ID
@router.get("/{sale_id}", response_model=Sale)
def read_sale(sale_id: int, db: Session = Depends(get_db)):
    db_sale = db.query(SaleModel).filter(SaleModel.id == sale_id).first()
    if db_sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return db_sale

# مسار لتحديث عملية بيع بناءً على ID (PUT)
@router.put("/{sale_id}", response_model=Sale)
def update_sale(sale_id: int, sale: SaleUpdate, db: Session = Depends(get_db)):
    db_sale = db.query(SaleModel).filter(SaleModel.id == sale_id).first()
    if db_sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")

    for key, value in sale.dict().items():
        setattr(db_sale, key, value)

    db.commit()
    db.refresh(db_sale)
    return db_sale

# مسار لحذف عملية بيع بناءً على ID (DELETE)
@router.delete("/{sale_id}", response_model=dict)
def delete_sale(sale_id: int, db: Session = Depends(get_db)):
    db_sale = db.query(SaleModel).filter(SaleModel.id == sale_id).first()
    if db_sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")

    db.delete(db_sale)
    db.commit()
    return {"message": "Sale deleted successfully"}
