from fastapi import FastAPI, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import schemas
import view
import models
from fastapi.responses import JSONResponse


# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    print(db)
    try:
        yield db
    finally:
        db.close()

# Depends - передача результата функции get_db.
@app.post("/api/create")
async def user_create(user: schemas.UserBase,
                      db: Session = Depends(get_db)):
    user = view.create_user(db=db, user=user)
    return JSONResponse(status_code=200, content={"user": f"{user}"})


@app.get("/api/users")
def get_people(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@app.post("/send")
def send_message(message: schemas.Message, db: Session = Depends(get_db),
                 id: str | None = Header(default=None)):
    print(id, 11111111111)
    sender_id = id
    recepient_id = view.get_user_by_id(db, message.recipient_id)
    print(recepient_id)
    if not recepient_id:
        return HTTPException(status_code=400, detail='Not found')

    return view.sending_message(db, sender_id, message)
