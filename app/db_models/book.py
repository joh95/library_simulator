from sqlalchemy import Boolean, Column, ForeignKey, Integer, Float, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    literary_genre = Column(String)
    author = Column(String)
    year = Column(String)
    price = Column(String)

    class Config:
        orm_mode = True
