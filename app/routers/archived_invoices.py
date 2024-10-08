from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.archived_invoices import ArchivedInvoice as ArchivedInvoiceModel
from app.schemas.archived_invoices_schemas import ArchivedInvoiceCreate, ArchivedInvoice

router = APIRouter()

# إضافة فاتورة مؤرشفة جديدة (POST)
@router.post("/", response_model=ArchivedInvoice)
def create_archived_invoice(invoice: ArchivedInvoiceCreate, db: Session = Depends(get_db)):
    db_invoice = ArchivedInvoiceModel(**invoice.dict())
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

# عرض جميع الفواتير المؤرشفة (GET)
@router.get("/", response_model=list[ArchivedInvoice])
def read_archived_invoices(db: Session = Depends(get_db)):
    return db.query(ArchivedInvoiceModel).all()

# عرض فاتورة مؤرشفة بناءً على ID (GET by ID)
@router.get("/{invoice_id}", response_model=ArchivedInvoice)
def read_archived_invoice(invoice_id: int, db: Session = Depends(get_db)):
    db_invoice = db.query(ArchivedInvoiceModel).filter(ArchivedInvoiceModel.id == invoice_id).first()
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Archived invoice not found")
    return db_invoice

# تحديث فاتورة مؤرشفة (PUT)
@router.put("/{invoice_id}", response_model=ArchivedInvoice)
def update_archived_invoice(invoice_id: int, invoice: ArchivedInvoiceCreate, db: Session = Depends(get_db)):
    db_invoice = db.query(ArchivedInvoiceModel).filter(ArchivedInvoiceModel.id == invoice_id).first()
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Archived invoice not found")

    for key, value in invoice.dict().items():
        setattr(db_invoice, key, value)

    db.commit()
    db.refresh(db_invoice)
    return db_invoice

# حذف فاتورة مؤرشفة (DELETE)
@router.delete("/{invoice_id}", response_model=dict)
def delete_archived_invoice(invoice_id: int, db: Session = Depends(get_db)):
    db_invoice = db.query(ArchivedInvoiceModel).filter(ArchivedInvoiceModel.id == invoice_id).first()
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Archived invoice not found")

    db.delete(db_invoice)
    db.commit()
    return {"message": "Archived invoice deleted successfully"}
