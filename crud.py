from sqlalchemy.orm import Session
import models, schemas

def get_game(db: Session):
    return db.query(models.Game).all()