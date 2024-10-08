from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.audit_logs import AuditLog as AuditLogModel
from app.schemas.audit_logs_schemas import AuditLogCreate, AuditLog

router = APIRouter()

# إضافة سجل جديد (POST)
@router.post("/", response_model=AuditLog)
def create_audit_log(audit_log: AuditLogCreate, db: Session = Depends(get_db)):
    db_audit_log = AuditLogModel(**audit_log.dict())
    db.add(db_audit_log)
    db.commit()
    db.refresh(db_audit_log)
    return db_audit_log

# عرض جميع السجلات (GET)
@router.get("/", response_model=list[AuditLog])
def read_audit_logs(db: Session = Depends(get_db)):
    return db.query(AuditLogModel).all()

# عرض السجلات بناءً على الموظف أو الجدول أو نوع الإجراء (GET)
@router.get("/filter", response_model=list[AuditLog])
def filter_audit_logs(employee_id: int = None, table_name: str = None, action_type: str = None, db: Session = Depends(get_db)):
    query = db.query(AuditLogModel)
    if employee_id:
        query = query.filter(AuditLogModel.employee_id == employee_id)
    if table_name:
        query = query.filter(AuditLogModel.table_name == table_name)
    if action_type:
        query = query.filter(AuditLogModel.action_type == action_type)
    return query.all()
