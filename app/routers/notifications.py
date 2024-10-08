from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.notifications import Notification as NotificationModel
from app.schemas.notifications_schemas import NotificationCreate, Notification

router = APIRouter()

# مسار لإضافة إشعار جديد (POST)
@router.post("/", response_model=Notification)
def create_notification(notification: NotificationCreate, db: Session = Depends(get_db)):
    db_notification = NotificationModel(**notification.dict())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

# مسار للحصول على جميع الإشعارات (GET)
@router.get("/", response_model=list[Notification])
def read_notifications(db: Session = Depends(get_db)):
    return db.query(NotificationModel).all()

# مسار للحصول على إشعار معين بناءً على ID (GET by ID)
@router.get("/{notification_id}", response_model=Notification)
def read_notification(notification_id: int, db: Session = Depends(get_db)):
    db_notification = db.query(NotificationModel).filter(NotificationModel.id == notification_id).first()
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return db_notification

# مسار لتحديث حالة الإشعار (PUT)
@router.put("/{notification_id}", response_model=Notification)
def update_notification(notification_id: int, notification: NotificationCreate, db: Session = Depends(get_db)):
    db_notification = db.query(NotificationModel).filter(NotificationModel.id == notification_id).first()
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")

    for key, value in notification.dict().items():
        setattr(db_notification, key, value)

    db.commit()
    db.refresh(db_notification)
    return db_notification

# مسار لتحديث حالة الإشعار إلى مقروء (PATCH)
@router.patch("/{notification_id}/read", response_model=Notification)
def mark_notification_as_read(notification_id: int, db: Session = Depends(get_db)):
    db_notification = db.query(NotificationModel).filter(NotificationModel.id == notification_id).first()
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")

    db_notification.is_read = True
    db.commit()
    db.refresh(db_notification)
    return db_notification

# مسار لحذف إشعار بناءً على ID (DELETE)
@router.delete("/{notification_id}", response_model=dict)
def delete_notification(notification_id: int, db: Session = Depends(get_db)):
    db_notification = db.query(NotificationModel).filter(NotificationModel.id == notification_id).first()
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")

    db.delete(db_notification)
    db.commit()
    return {"message": "Notification deleted successfully"}
