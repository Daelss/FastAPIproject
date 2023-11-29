from sqlalchemy.orm import Session
import models, schemas

def get_game(db: Session):
    return db.query(models.Game).all()

def get_developer(db: Session):
    return db.query(models.Developer).all()

def get_publisher(db: Session):
    return db.query(models.Publisher).all()

def get_platform(db: Session):
    return db.query(models.Platform).all()

def get_genre(db: Session):
    return db.query(models.Genre).all()