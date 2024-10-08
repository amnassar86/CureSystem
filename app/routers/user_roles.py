from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user_roles import UserRole as UserRoleModel
from app.schemas.user_role_schemas import UserRoleCreate, UserRole

router = APIRouter()

# مسار لإضافة دور جديد لموظف (POST)
@router.post("/", response_model=UserRole)
def create_user_role(user_role: UserRoleCreate, db: Session = Depends(get_db)):
    try:
        db_user_role = UserRoleModel(**user_role.dict())
        db.add(db_user_role)
        db.commit()
        db.refresh(db_user_role)
        return db_user_role
    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=400, detail="Failed to assign role to employee")

# مسار للحصول على جميع الأدوار المرتبطة بالموظفين (GET)
@router.get("/", response_model=list[UserRole])
def read_user_roles(db: Session = Depends(get_db)):
    try:
        user_roles = db.query(UserRoleModel).all()
        return user_roles
    except Exception as e:
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=400, detail="Failed to fetch user roles")

# مسار للحصول على دور معين لموظف بناءً على ID (GET by ID)
@router.get("/{user_role_id}", response_model=UserRole)
def read_user_role(user_role_id: int, db: Session = Depends(get_db)):
    db_user_role = db.query(UserRoleModel).filter(UserRoleModel.id == user_role_id).first()
    if db_user_role is None:
        raise HTTPException(status_code=404, detail="User role not found")
    return db_user_role

# مسار لتحديث دور الموظف بناءً على ID (PUT)
@router.put("/{user_role_id}", response_model=UserRole)
def update_user_role(user_role_id: int, user_role: UserRoleCreate, db: Session = Depends(get_db)):
    db_user_role = db.query(UserRoleModel).filter(UserRoleModel.id == user_role_id).first()
    if db_user_role is None:
        raise HTTPException(status_code=404, detail="User role not found")

    for key, value in user_role.dict(exclude_unset=True).items():
        setattr(db_user_role, key, value)

    db.commit()
    db.refresh(db_user_role)
    return db_user_role
# مسار لحذف دور موظف بناءً على ID (DELETE)
@router.delete("/{user_role_id}", response_model=dict)
def delete_user_role(user_role_id: int, db: Session = Depends(get_db)):
    db_user_role = db.query(UserRoleModel).filter(UserRoleModel.id == user_role_id).first()
    if db_user_role is None:
        raise HTTPException(status_code=404, detail="User role not found")

    db.delete(db_user_role)
    db.commit()
    return {"message": "User role deleted successfully"}

