from fastapi import FastAPI
from models import Game
from sqlalchemy.orm import Session
from database import engine
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


@app.get("/games/", response_model=List[schemas.Game])
def get_games(db: Session = Depends(get_db)):
    games = crud.get_game(db)
    return games

@app.get("/developer/", response_model=List[schemas.Developer])
def get_developer(db: Session = Depends(get_db)):
    developers = crud.get_developer(db)
    return developers

@app.get("/publisher/", response_model=List[schemas.Publisher])
def get_publisher(db: Session = Depends(get_db)):
    publisher = crud.get_developer(db)
    return publisher

@app.get("/platform/", response_model=List[schemas.Platform])
def get_platform(db: Session = Depends(get_db)):
    platform = crud.get_developer(db)
    return platform

@app.get("/genre/", response_model=List[schemas.Genre])
def get_platform(db: Session = Depends(get_db)):
    genre = crud.get_developer(db)
    return genre