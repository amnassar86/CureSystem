from pydantic import BaseModel
from typing import Optional
from datetime import time

# نموذج أساسي للوردية
class ShiftBase(BaseModel):
    shift_name: Optional[str] = None
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    employee_id: Optional[int] = None

# نموذج لإنشاء وردية جديدة
class ShiftCreate(ShiftBase):
    pass

# نموذج لعرض بيانات الوردية
class Shift(ShiftBase):
    id: int

    class Config:
        from_attributes = True

# نموذج لتحديث بيانات الوردية
class ShiftUpdate(BaseModel):
    shift_name: Optional[str] = None
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    employee_id: Optional[int] = None
