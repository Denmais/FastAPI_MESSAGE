from sqlalchemy.orm import Session
import models, schemas


def create_user(db: Session, user: schemas.UserBase):
    db_user = models.User(username=user.username,
                          email=user.email,
                          password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).all()


def sending_message(db: Session, send_id: int, message: schemas.Message):
    db_message = models.Message(text=message.text,
                                sender_id=send_id,
                                recipient_id=message.recipient_id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


