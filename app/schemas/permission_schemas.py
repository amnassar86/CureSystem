from pydantic import BaseModel

# نموذج أساسي للصلاحية
class PermissionBase(BaseModel):
    permission_name: str

# نموذج لإنشاء صلاحية جديدة
class PermissionCreate(PermissionBase):
    pass

# نموذج لعرض بيانات الصلاحية
class Permission(PermissionBase):
    id: int

    class Config:
        from_attributes = True

# نموذج لتحديث بيانات الصلاحية
class PermissionUpdate(BaseModel):
    permission_name: str
