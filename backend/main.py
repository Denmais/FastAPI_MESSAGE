from fastapi import FastAPI, Depends
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
