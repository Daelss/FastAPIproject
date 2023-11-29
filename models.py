from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Game(Base):
    __tablename__ = 'game'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    developer_id = Column(Integer, ForeignKey('developer.id'))
    developer = relationship('Developer', back_populates="dev")
    publisher_id = Column(Integer, ForeignKey('publisher.id'))
    publisher = relationship('Publisher', back_populates="pub")
    genre_id = Column(Integer, ForeignKey('genre.id'))
    genre = relationship('Genre', back_populates="gen")
    platform_id = Column(Integer, ForeignKey('platform.id'))
    platforms = relationship('Platform', back_populates="plat")



class Developer(Base):
    __tablename__ = 'developer'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)



    dev = relationship("Game", back_populates="developer")



class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, unique=True, nullable=False)



    pub = relationship("Game", back_populates="publisher")

class Platform(Base):
    __tablename__ = 'platform'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)



    plat = relationship("Game", back_populates="platforms")
class Genre(Base):
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)



    gen = relationship("Game", back_populates="genre")

