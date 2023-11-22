from sqlalchemy import Column, ForeignKey, String, Integer, Boolean, ForeignKey, Date, Float, Table, MetaData
from sqlalchemy.orm import relationship

from database import Base


class Game(Base):
    __tablename__ = 'game'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    developer_id = Column(ForeignKey('developers.id'))
    developer = relationship('Developer')
    publisher_id = Column(ForeignKey('publishers.id'))
    publisher = relationship('Publisher')
    release_date = Column(Date)
    genre_id = Column(ForeignKey('genres.id'))
    genre = relationship('Genre')
    platform_id = Column(ForeignKey('platforms.id'))
    platforms = relationship('Platform')

    def __repr__(self):
        return f'<Game {self.title} >'

class Developer(Base):
    __tablename__ = 'developer'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f'<Developer {self.name}>'

class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f'<Publisher {self.name}>'

class Platform(Base):
    __tablename__ = 'platform'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f'<Platform {self.name}>'

class Genre(Base):
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f'<Genre {self.name}>'


