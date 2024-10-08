from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.role_permissions import RolePermission as RolePermissionModel
from app.schemas.role_permission_schemas import RolePermissionCreate, RolePermission

router = APIRouter()

# مسار لإضافة دور وصلاحية جديدة (POST)
@router.post("/", response_model=RolePermission)
def create_role_permission(role_permission: RolePermissionCreate, db: Session = Depends(get_db)):
    try:
        db_role_permission = RolePermissionModel(**role_permission.dict())
        db.add(db_role_permission)
        db.commit()
        db.refresh(db_role_permission)
        return db_role_permission
    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=400, detail="Failed to create role permission")

# مسار للحصول على جميع الأدوار والصلاحيات (GET)
@router.get("/", response_model=list[RolePermission])
def read_role_permissions(db: Session = Depends(get_db)):
    try:
        role_permissions = db.query(RolePermissionModel).all()
        return role_permissions
    except Exception as e:
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=400, detail="Failed to fetch role permissions")

# مسار للحصول على دور وصلاحية معينة بناءً على ID (GET by ID)
@router.get("/{role_permission_id}", response_model=RolePermission)
def read_role_permission(role_permission_id: int, db: Session = Depends(get_db)):
    db_role_permission = db.query(RolePermissionModel).filter(RolePermissionModel.id == role_permission_id).first()
    if db_role_permission is None:
        raise HTTPException(status_code=404, detail="Role Permission not found")
    return db_role_permission

# مسار لتحديث ارتباط دور وصلاحية بناءً على ID (PUT)
@router.put("/{role_permission_id}", response_model=RolePermission)
def update_role_permission(role_permission_id: int, role_permission: RolePermissionCreate, db: Session = Depends(get_db)):
    db_role_permission = db.query(RolePermissionModel).filter(RolePermissionModel.id == role_permission_id).first()
    if db_role_permission is None:
        raise HTTPException(status_code=404, detail="Role Permission not found")

    for key, value in role_permission.dict(exclude_unset=True).items():
        setattr(db_role_permission, key, value)

    db.commit()
    db.refresh(db_role_permission)
    return db_role_permission


# مسار لحذف دور وصلاحية بناءً على ID (DELETE)
@router.delete("/{role_permission_id}", response_model=dict)
def delete_role_permission(role_permission_id: int, db: Session = Depends(get_db)):
    db_role_permission = db.query(RolePermissionModel).filter(RolePermissionModel.id == role_permission_id).first()
    if db_role_permission is None:
        raise HTTPException(status_code=404, detail="Role Permission not found")

    db.delete(db_role_permission)
    db.commit()
    return {"message": "Role Permission deleted successfully"}
