from pydantic import BaseModel
from datetime import datetime

class AuditLogBase(BaseModel):
    employee_id: int
    action_type: str
    table_name: str
    record_id: int
    old_data: str | None = None
    new_data: str | None = None
    ip_address: str | None = None
    device_info: str | None = None

class AuditLogCreate(AuditLogBase):
    pass

class AuditLog(AuditLogBase):
    id: int
    action_date: datetime

    class Config:
        orm_mode = True
