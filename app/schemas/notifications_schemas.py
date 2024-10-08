from pydantic import BaseModel
from datetime import datetime

class NotificationBase(BaseModel):
    message: str
    notification_type: str
    medication_id: int | None = None
    employee_id: int | None = None
    priority: str | None = 'medium'
    target_type: str | None = 'pharmacist'

class NotificationCreate(NotificationBase):
    pass

class Notification(NotificationBase):
    id: int
    created_at: datetime
    is_read: bool

    class Config:
        orm_mode = True
