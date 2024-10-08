from pydantic import BaseModel

# نموذج أساسي للدور
class RoleBase(BaseModel):
    role_name: str

# نموذج لإنشاء دور جديد
class RoleCreate(RoleBase):
    pass

# نموذج لعرض بيانات الدور
class Role(RoleBase):
    id: int

    class Config:
        from_attributes = True

# نموذج لتحديث بيانات الدور
class RoleUpdate(BaseModel):
    role_name: str
