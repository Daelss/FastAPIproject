from fastapi import FastAPI
from models import Game
from sqlalchemy.orm import Session
from database import engine
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

app = FastAPI()

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


@app.get("/games/", response_model=List[schemas.Game])
def read_users(db: Session = Depends(get_db)):
    games = crud.get_game(db)
    return games