from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.roles import Role as RoleModel
from app.schemas.role_schemas import RoleCreate, Role, RoleUpdate

router = APIRouter()

# مسار لإضافة دور جديد (POST)
@router.post("/", response_model=Role)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    try:
        db_role = RoleModel(**role.dict())
        db.add(db_role)
        db.commit()
        db.refresh(db_role)
        return db_role
    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=400, detail="Failed to create role")

# مسار للحصول على جميع الأدوار (GET)
@router.get("/", response_model=list[Role])
def read_roles(db: Session = Depends(get_db)):
    try:
        roles = db.query(RoleModel).all()
        return roles
    except Exception as e:
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=400, detail="Failed to fetch roles")

# مسار للحصول على دور معين بناءً على ID (GET by ID)
@router.get("/{role_id}", response_model=Role)
def read_role(role_id: int, db: Session = Depends(get_db)):
    db_role = db.query(RoleModel).filter(RoleModel.id == role_id).first()
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

# مسار لتحديث دور بناءً على ID (PUT)
@router.put("/{role_id}", response_model=Role)
def update_role(role_id: int, role: RoleUpdate, db: Session = Depends(get_db)):
    db_role = db.query(RoleModel).filter(RoleModel.id == role_id).first()
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")

    for key, value in role.dict(exclude_unset=True).items():
        setattr(db_role, key, value)

    db.commit()
    db.refresh(db_role)
    return db_role

# مسار لحذف دور بناءً على ID (DELETE)
@router.delete("/{role_id}", response_model=dict)
def delete_role(role_id: int, db: Session = Depends(get_db)):
    db_role = db.query(RoleModel).filter(RoleModel.id == role_id).first()
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")

    db.delete(db_role)
    db.commit()
    return {"message": "Role deleted successfully"}
