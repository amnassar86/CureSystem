from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.permissions import Permission as PermissionModel
from app.schemas.permission_schemas import PermissionCreate, Permission, PermissionUpdate

router = APIRouter()

# مسار لإضافة صلاحية جديدة (POST)
@router.post("/", response_model=Permission)
def create_permission(permission: PermissionCreate, db: Session = Depends(get_db)):
    try:
        db_permission = PermissionModel(**permission.dict())
        db.add(db_permission)
        db.commit()
        db.refresh(db_permission)
        return db_permission
    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=400, detail="Failed to create permission")

# مسار للحصول على جميع الصلاحيات (GET)
@router.get("/", response_model=list[Permission])
def read_permissions(db: Session = Depends(get_db)):
    try:
        permissions = db.query(PermissionModel).all()
        return permissions
    except Exception as e:
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=400, detail="Failed to fetch permissions")

# مسار للحصول على صلاحية معينة بناءً على ID (GET by ID)
@router.get("/{permission_id}", response_model=Permission)
def read_permission(permission_id: int, db: Session = Depends(get_db)):
    db_permission = db.query(PermissionModel).filter(PermissionModel.id == permission_id).first()
    if db_permission is None:
        raise HTTPException(status_code=404, detail="Permission not found")
    return db_permission

# مسار لتحديث صلاحية بناءً على ID (PUT)
@router.put("/{permission_id}", response_model=Permission)
def update_permission(permission_id: int, permission: PermissionUpdate, db: Session = Depends(get_db)):
    db_permission = db.query(PermissionModel).filter(PermissionModel.id == permission_id).first()
    if db_permission is None:
        raise HTTPException(status_code=404, detail="Permission not found")

    for key, value in permission.dict(exclude_unset=True).items():
        setattr(db_permission, key, value)

    db.commit()
    db.refresh(db_permission)
    return db_permission

# مسار لحذف صلاحية بناءً على ID (DELETE)
@router.delete("/{permission_id}", response_model=dict)
def delete_permission(permission_id: int, db: Session = Depends(get_db)):
    db_permission = db.query(PermissionModel).filter(PermissionModel.id == permission_id).first()
    if db_permission is None:
        raise HTTPException(status_code=404, detail="Permission not found")

    db.delete(db_permission)
    db.commit()
    return {"message": "Permission deleted successfully"}
