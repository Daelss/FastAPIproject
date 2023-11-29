from pydantic import BaseModel


class GameBase(BaseModel):
    title: str


class GameCreate(GameBase):
    pass

class Game(GameBase):
    developer_id: int
    publisher_id: int
    genre_id: int
    platform_id: int



    class Config:
        from_attributes = True


class DeveloperBase(BaseModel):
    id: int
    name: str

class DeveloperCreate(DeveloperBase):
    pass

class Developer(DeveloperBase):
    name: str
    dev: list[Game] = []

    class Config:
        from_attributes = True


class PublisherBase(BaseModel):
    id: int
    name: str

class PublisherCreate(PublisherBase):
    pass

class Publisher(DeveloperBase):
    name: str
    pub: list[Game] = []
    class Config:
        from_attributes = True

class PlatformBase(BaseModel):
    id: int
    name: str

class PlatformCreate(PlatformBase):
    pass

class Platform(PlatformBase):
    name: str
    plat: list[Game] = []
    class Config:
        from_attributes = True


class GenreBase(BaseModel):
    id: int
    name: str

class GenreCreate(GenreBase):
    pass

class Genre(GenreBase):
    name: str
    gen: list[Game] = []
    class Config:
        from_attributes = True

