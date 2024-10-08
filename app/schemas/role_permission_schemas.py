from pydantic import BaseModel

# نموذج أساسي للأدوار والصلاحيات
class RolePermissionBase(BaseModel):
    role_id: int
    permission_id: int

# نموذج لإنشاء دور وصلاحية جديدة
class RolePermissionCreate(RolePermissionBase):
    pass

# نموذج لعرض بيانات دور وصلاحية
class RolePermission(RolePermissionBase):
    id: int

    class Config:
        from_attributes = True
