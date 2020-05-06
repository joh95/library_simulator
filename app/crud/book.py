from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.db_models.book import Book
from app.models.book import BookCreate, BookUpdate


def get_by_id(db_session: Session, *, book_id: int) -> Optional[Book]:
    return db_session.query(Book).filter(Book.id == book_id).first()


def get_multiple_book(*, db_session: Session) -> List[Optional[Book]]:
    return db_session.query(Book).all()

def get_by_name(db_session: Session, *, name: str) -> Optional[Book]:
    return db_session.query(Book).filter(Book.name == name).first()

def get_by_author(db_session: Session, *, author: str) -> Optional[Book]:
    return db_session.query(Book).filter(Book.author == author).all()

def create(db_session: Session, *, book_in: BookCreate) -> Book:
    book_in_data = jsonable_encoder(book_in)
    book = Book(**book_in_data)
    db_session.add(book)
    db_session.commit()
    db_session.refresh(book)
    return book


def update(db_session: Session, *, book: Book, book_in: BookUpdate) -> Book:
    book_data = jsonable_encoder(book)
    update_data = book_in.dict(skip_defaults=True)
    for field in book_data:
        if field in update_data:
            setattr(book, field, update_data[field])
    db_session.add(book)
    db_session.commit()
    db_session.refresh(book)
    return book


def remove(db_session: Session, *, book_id: int):
    book = db_session.query(Book).filter(Book.id == book_id).first()
    db_session.delete(book)
    db_session.commit()
    return book
