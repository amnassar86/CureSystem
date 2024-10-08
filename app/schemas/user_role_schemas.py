from pydantic import BaseModel

# نموذج أساسي لأدوار الموظفين
class UserRoleBase(BaseModel):
    employee_id: int
    role_id: int

# نموذج لإنشاء دور لموظف جديد
class UserRoleCreate(UserRoleBase):
    pass

# نموذج لعرض بيانات دور الموظف
class UserRole(UserRoleBase):
    id: int

    class Config:
        from_attributes = True
