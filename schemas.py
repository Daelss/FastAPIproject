from pydantic import BaseModel


class GameBase(BaseModel):
    title: str
    description: str

class GameCreate(GameBase):
    pass

class Game(GameBase):
    developer: str
    publisher: str
    release_date: int
    genre: list[str]
    rating: int
    platform: str


    class Config:
        orm_mode = True


class DeveloperBase(BaseModel):
    id: int
    name: str

class DeveloperCreate(DeveloperBase):
    pass

class Developer(DeveloperBase):
    name: str

    class Config:
        orm_mode = True


class PublisherBase(BaseModel):
    id: int
    name: str

class PublisherCreate(PublisherBase):
    pass

class Publisher(DeveloperBase):
    name: str

    class Config:
        orm_mode = True

class PlatformBase(BaseModel):
    id: int
    name: str

class PlatformCreate(PlatformBase):
    pass

class Platform(PlatformBase):
    name: str

    class Config:
        orm_mode = True


class GenreBase(BaseModel):
    id: int
    name: str

class GenreCreate(GenreBase):
    pass

class Genre(GenreBase):
    name: str

    class Config:
        orm_mode = True

